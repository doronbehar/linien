# Copyright 2023 Bastian Leykauf <leykauf@physik.hu-berlin.de>
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

import json
import logging
from dataclasses import dataclass

from .config import USER_DATA_PATH

CREDENTIAL_STORE_FILENAME = "influxdb_credentials.json"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass
class InfluxDBCredentials:
    url: str = "http://localhost:8086"
    org: str = "my-org"
    token: str = "my-token"
    bucket: str = "my-bucket"
    measurement: str = "my-measurement"


def save_credentials(credentials: InfluxDBCredentials) -> None:
    """Save the credentials to disk."""
    filename = str(USER_DATA_PATH / CREDENTIAL_STORE_FILENAME)
    with open(filename, "w") as f:
        json.dump(
            {
                "url": credentials.url,
                "org": credentials.org,
                "token": credentials.token,
                "bucket": credentials.bucket,
                "measurement": credentials.measurement,
            },
            f,
            indent=2,
        )
    logger.info(f"Saved InfluxDB credentials to {filename}")


def restore_credentials() -> InfluxDBCredentials:
    """When the server starts, it tries to restore the credentials."""
    filename = USER_DATA_PATH / CREDENTIAL_STORE_FILENAME
    try:
        with open(str(filename), "r") as f:
            data = json.load(f)
        return InfluxDBCredentials(
            url=data["url"],
            org=data["org"],
            token=data["token"],
            bucket=data["bucket"],
            measurement=data["measurement"],
        )
    except FileNotFoundError:
        return InfluxDBCredentials()
    except json.JSONDecodeError:
        # get a unice filename
        i = 0
        while True:
            backup_filename = (
                filename.parent / f"{CREDENTIAL_STORE_FILENAME.stem}.backup{i}"
            )
            if not backup_filename.exists():
                break
            i += 1

        filename.rename(backup_filename)
        logger.error(
            f"{filename} was corrupted. Using default parameters. Corrupted file has "
            f"been saved as {backup_filename}."
        )
        return InfluxDBCredentials()
