# Copyright 2024 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A small cli tool for use to precompile py source files

Args:
    src_path: str, source py file path
    pyc_path: str, file path where pyc should be written to
    invalidation_mode: str, mode to determine compilation based on PycInvalidationMode. Currently one of [UNCHECKED_HASH, CHECKED_HASH]
"""
from sys import argv
from py_compile import compile, PycInvalidationMode

def main():
    src_path = arg[1]
    pyc_path = arg[2]
    invalidation_mode = arg[3]

    pyc_invalidation_mode = {
        "UNCHECKED_HASH": PycInvalidationMode.UNCHECKED_HASH,
        "CHECKED_HASH": PycInvalidationMode.CHECKED_HASH,
    }
    if invalidation_mode not in pyc_invalidation_mode:
        raise RuntimeError(f"{invalidation_mode} is not a valid choice. Choose 1 of {pyc_invalidation_mode.keys()}")

    compile(argv1, cfile=argv[2], invalidation_mode=pyc_invalidation_mode[invalidation_mode])

if __name__ == "__main__":
    main()