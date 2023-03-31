# Copyright 2018-2022 Benjamin Wiegand <benjamin.wiegand@physik.hu-berlin.de>
# Copyright 2021-2023 Bastian Leykauf <leykauf@physik.hu-berlin.de>
#
# This file is part of Linien and based on redpid.
#
# Linien is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linien is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linien.  If not, see <http://www.gnu.org/licenses/>.

import _thread
import os
import pickle
import sys
import threading
from random import randint, random
from time import sleep

import click
import numpy as np
import rpyc
from linien_common.common import (
    N_POINTS,
    check_plot_data,
    pack,
    unpack,
    update_signal_history,
)
from linien_common.config import DEFAULT_SERVER_PORT
from linien_server import __version__
from linien_server.autolock.autolock import Autolock
from linien_server.optimization.optimization import OptimizeSpectroscopy
from linien_server.parameters import Parameters, ParameterStore
from linien_server.pid_optimization.pid_optimization import (
    PIDOptimization,
    PSDAcquisition,
)
from linien_server.registers import Registers
from rpyc.utils.authenticators import AuthenticationError
from rpyc.utils.server import ThreadedServer


class BaseService(rpyc.Service):
    """
    A service that provides functionality for seamless integration of parameter access
    on the client.
    """

    def __init__(self):
        self.parameters = Parameters()
        self.parameter_store = ParameterStore(self.parameters)
        self._uuid_mapping = {}

    def on_connect(self, client):
        self._uuid_mapping[client] = client.root.uuid

    def on_disconnect(self, client):
        uuid = self._uuid_mapping[client]
        self.parameters.unregister_remote_listeners(uuid)

    def exposed_get_server_version(self):
        return __version__

    def exposed_get_param(self, param_name):
        return pack(self.parameters._get_param(param_name).value)

    def exposed_set_param(self, param_name, value):
        self.parameters._get_param(param_name).value = unpack(value)

    def exposed_init_parameter_sync(self, uuid):
        return pack(list(self.parameters.init_parameter_sync(uuid)))

    def exposed_register_remote_listener(self, uuid, param_name):
        return self.parameters.register_remote_listener(uuid, param_name)

    def exposed_register_remote_listeners(self, uuid, param_names):
        for param_name in param_names:
            self.exposed_register_remote_listener(uuid, param_name)

    def exposed_get_listener_queue(self, uuid):
        return self.parameters.get_listener_queue(uuid)


class RedPitayaControlService(BaseService):
    """Control server that runs on the RP that provides high-level methods."""

    def __init__(self, host=None):
        self._cached_data = {}
        self.exposed_is_locked = None

        super(RedPitayaControlService, self).__init__()

        self.registers = Registers(control=self, parameters=self.parameters, host=host)
        self._connect_acquisition_to_parameters()
        self._start_periodic_timer()
        self.exposed_write_registers()

    def _connect_acquisition_to_parameters(self):
        """
        Connect the acquisition loopo to the parameters: Every received value is pushed
        to `parameters.to_plot`.
        """
        # each time new data is acquired, this function is called
        self.registers.acquisition_controller.on_new_data_received = (
            self._on_new_data_received
        )
        self.pause_acquisition()
        self.continue_acquisition()

    def _on_new_data_received(self, is_raw, plot_data, data_uuid):
        # When a parameter is changed, `pause_acquisition` is set. This means that
        # the we should skip new data until we are sure that it was recorded with
        # the new settings.
        if not self.parameters.pause_acquisition.value:
            if data_uuid != self.data_uuid:
                return

            data_loaded = pickle.loads(plot_data)

            if not is_raw:
                is_locked = self.parameters.lock.value

                if not check_plot_data(is_locked, data_loaded):
                    print("warning: incorrect data received for lock state, ignoring!")
                    return

                self.parameters.to_plot.value = plot_data
                self._generate_signal_stats(data_loaded)

                # update signal history (if in locked state)
                (
                    self.parameters.control_signal_history.value,
                    self.parameters.monitor_signal_history.value,
                ) = update_signal_history(
                    self.parameters.control_signal_history.value,
                    self.parameters.monitor_signal_history.value,
                    data_loaded,
                    is_locked,
                    self.parameters.control_signal_history_length.value,
                )
            else:
                self.parameters.acquisition_raw_data.value = plot_data

    def _start_periodic_timer(self):
        """
        Start a timer that increases the `ping` parameter once per second. Its purpose
        is to allow for periodic tasks on the server: just register an `on_change`
        listener for this parameter.
        """

        def send_ping():
            while True:
                self.parameters.ping.value = self.parameters.ping.value + 1
                print("ping", self.parameters.ping.value)
                sleep(1)

        thread = threading.Thread(target=send_ping)
        thread.daemon = True
        thread.start()
        self._periodic_timer = thread

    def _generate_signal_stats(self, to_plot):
        stats = {}

        for signal_name, signal in to_plot.items():
            stats["%s_mean" % signal_name] = np.mean(signal)
            stats["%s_std" % signal_name] = np.std(signal)
            stats["%s_max" % signal_name] = np.max(signal)
            stats["%s_min" % signal_name] = np.min(signal)

        self.parameters.signal_stats.value = stats

    def exposed_write_registers(self):
        """Sync the parameters with the FPGA registers."""
        self.registers.write_registers()

    def task_running(self):
        return (
            self.parameters.autolock_running.value
            or self.parameters.optimization_running.value
            or self.parameters.psd_acquisition_running.value
            or self.parameters.psd_optimization_running.value
        )

    def exposed_start_autolock(self, x0, x1, spectrum, additional_spectra=None):
        spectrum = pickle.loads(spectrum)
        # start_watching = self.parameters.watch_lock.value
        start_watching = False
        auto_offset = self.parameters.autolock_determine_offset.value

        if not self.task_running():
            autolock = Autolock(self, self.parameters)
            self.parameters.task.value = autolock
            autolock.run(
                x0,
                x1,
                spectrum,
                should_watch_lock=start_watching,
                auto_offset=auto_offset,
                additional_spectra=pickle.loads(additional_spectra)
                if additional_spectra is not None
                else None,
            )

    def exposed_start_optimization(self, x0, x1, spectrum):
        if not self.task_running():
            optim = OptimizeSpectroscopy(self, self.parameters)
            self.parameters.task.value = optim
            optim.run(x0, x1, spectrum)

    def exposed_start_psd_acquisition(self):
        if not self.task_running():
            self.parameters.task.value = PSDAcquisition(self, self.parameters)
            self.parameters.task.value.run()

    def exposed_start_pid_optimization(self):
        if not self.task_running():
            self.parameters.task.value = PIDOptimization(self, self.parameters)
            self.parameters.task.value.run()

    def exposed_start_sweep(self):
        self.pause_acquisition()

        self.parameters.combined_offset.value = 0
        self.parameters.lock.value = False
        self.exposed_write_registers()

        self.continue_acquisition()

    def exposed_start_lock(self):
        self.pause_acquisition()

        self.parameters.lock.value = True
        self.exposed_write_registers()

        self.continue_acquisition()

    def exposed_shutdown(self):
        """Kill the server."""
        self.registers.acquisition_controller.shutdown()
        _thread.interrupt_main()
        # we use SystemExit instead of os._exit because we want to call atexit handlers
        raise SystemExit

    def exposed_get_restorable_parameters(self):
        return self.parameters._restorable_parameters

    def exposed_pause_acquisition(self):
        self.pause_acquisition()

    def exposed_continue_acquisition(self):
        self.continue_acquisition()

    def exposed_set_csr_direct(self, k, v):
        """
        Directly sets a CSR register. This method is intended for debugging. Normally,
        the FPGA should be controlled via manipulation of parameters.
        """
        self.registers.set(k, v)

    def pause_acquisition(self):
        """
        Pause continuous acquisition. Call this before changing a parameter that alters
        the error / control signal. This way, no inconsistent signals reach the
        application. After setting the new parameter values, call
        `continue_acquisition`.
        """
        self.parameters.pause_acquisition.value = True
        self.data_uuid = random()
        self.registers.acquisition_controller.pause_acquisition()

    def continue_acquisition(self):
        """
        Continue acquisition after a short delay, when we are sure that the new
        parameters values have been written to the FPGA and that data that is now
        recorded is recorded with the correct parameters.
        """
        self.parameters.pause_acquisition.value = False
        self.registers.acquisition_controller.continue_acquisition(self.data_uuid)


class FakeRedPitayaControlService(BaseService):
    def __init__(self):
        super().__init__()
        self.exposed_is_locked = None

        self._connect_acquisition_to_parameters()

    def exposed_write_registers(self):
        pass

    def _connect_acquisition_to_parameters(self):
        def write_random_data_to_parameters():
            while True:
                max_ = randint(0, 8191)
                gen = lambda: np.array([randint(-max_, max_) for _ in range(N_POINTS)])
                self.parameters.to_plot.value = pickle.dumps(
                    {
                        "error_signal_1": gen(),
                        "error_signal_1_quadrature": gen(),
                        "error_signal_2": gen(),
                        "error_signal_2_quadrature": gen(),
                    }
                )
                sleep(0.1)

        thread = threading.Thread(target=write_random_data_to_parameters)
        thread.daemon = True
        thread.start()

    def exposed_shutdown(self):
        _thread.interrupt_main()
        os._exit(0)

    def exposed_start_autolock(self, x0, x1, spectrum):
        print("start autolock", x0, x1)

    def exposed_start_optimization(self, x0, x1, spectrum):
        print("start optimization")
        self.parameters.optimization_running.value = True

    def exposed_get_restorable_parameters(self):
        return self.parameters._restorable_parameters

    def pause_acquisition(self):
        pass

    def continue_acquisition(self):
        pass


def authenticate_username_and_password(sock):
    failed_auth_counter = {"c": 0}
    # when a client starts the server, it supplies this hash via an environment
    # variable
    secret = os.environ.get("LINIEN_AUTH_HASH")
    # client always sends auth hash, even if we run in non-auth mode --> always read
    # 64 bytes, otherwise rpyc connection can't be established
    received = sock.recv(64)
    # as a protection against brute force, we don't accept requests after too many
    # failed auth requests
    if failed_auth_counter["c"] > 1000:
        print("received too many failed auth requests!")
        sys.exit(1)

    if secret is None:
        print("warning: no authentication set up")
    else:
        if received != secret.encode():
            print("received invalid credentials: ", received)
            failed_auth_counter["c"] += 1
            raise AuthenticationError("invalid username / password")
        print("authentication successful")
    return sock, None


@click.command()
@click.version_option(__version__)
@click.argument("port", default=DEFAULT_SERVER_PORT, type=int, required=False)
@click.option(
    "--fake", is_flag=True, help="Runs a fake server that just returns random data"
)
@click.option(
    "--host",
    help=(
        "Allows to run the server locally for development and connects to a RedPitaya. "
        "Specify the RP's host as follows: --host=rp-f0xxxx.local"
    ),
)
def run_server(port, fake=False, host=None):
    print("Start server on port", port)

    if fake:
        print("starting fake server")
        control = FakeRedPitayaControlService()
    else:
        control = RedPitayaControlService(host=host)

    thread = ThreadedServer(
        control,
        port=port,
        authenticator=authenticate_username_and_password,
        protocol_config={"allow_pickle": True},
    )
    thread.start()


if __name__ == "__main__":
    run_server()
