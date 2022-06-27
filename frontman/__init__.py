#
# Copyright 2020 Chris Myers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import configparser
import logging
from logging.config import fileConfig

import proxy


class FrontmanConfig:
    """ configuration for frontman proxy """

    # TODO change to a config parser format

    config = configparser.ConfigParser()
    config.read('frontman.ini')

    mongo_index = config['core']['mongo_index']

    def __init__(self, cache_directory: str, force_recache: bool):
        self._cache_directory: str = cache_directory
        self._force_recache: bool = force_recache
        # , max_process: int = 5,
        #                  cache_directory: str = 'frontman', force_recache: bool = False

class FrontmanServer:
    """ proxy server for frontman """

    def __init__(self, host: str = 'localhost', port: int = 33333, max_backlog: int = 10):
        """ init method for server """

        # reads the local log configuration
        fileConfig('logging.ini')


