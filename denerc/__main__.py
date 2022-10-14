"""
Copyright (c) 2022 Dener and Dener Contributors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import uuid
from denerc.errors import UnsupportedOS

node_id = hex(uuid.uuid4().int)

if os.name != 'nt':
    raise UnsupportedOS(0, 'This OS is not supported yet.')

# TODO: CLI
# NOTE: CLI will most likely be just a complex toolchain
# for Package Managers to use and manage.
