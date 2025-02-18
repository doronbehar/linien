# Copyright 2018-2022 Benjamin Wiegand <benjamin.wiegand@physik.hu-berlin.de>
# Copyright 2021-2022 Bastian Leykauf <leykauf@physik.hu-berlin.de>
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
from urllib.request import urlopen

import linien_gui
from packaging import version
from PyQt5.QtCore import QThread, pyqtSignal


class VersionCheckerThread(QThread):
    check_done = pyqtSignal(bool)

    def run(self):
        our_version = version.parse(linien_gui.__version__)
        latest_version = our_version
        print("Check whether new version is available.")
        url = "https://raw.githubusercontent.com/linien-org/linien/master/version-info.json"  # noqa: E501
        try:
            with urlopen(url) as response:
                response_content = json.loads(response.read())
                latest_version = version.parse(response_content["latest"])
        finally:
            self.check_done.emit(latest_version > our_version)
