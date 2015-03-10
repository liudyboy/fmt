#!/usr/bin/env python
# Build the project on AppVeyor.

import os
from subprocess import check_call

build = os.environ['BUILD']
config = os.environ['CONFIG']
cmake_command = ['cmake', '-DFMT_EXTRA_TESTS=ON', '-DCMAKE_BUILD_TYPE=' + config]
if build == 'mingw':
  cmake_command.append('-GMinGW Makefiles')
  build_command = ['mingw32-make', '-j4']
  test_command = ['mingw32-make', 'test']
  # Remove the path to Git bin directory from $PATH because it breaks MinGW config.
  os.environ['PATH'] = os.environ['PATH'].replace(r'C:\Program Files (x86)\Git\bin', '')
else:
  build_command = ['msbuild', '/m:4', '/p:Config=' + config, 'FORMAT.sln']
  test_command = ['msbuild', 'RUN_TESTS.vcxproj']

check_call(cmake_command)
check_call(build_command)
check_call(test_command)
