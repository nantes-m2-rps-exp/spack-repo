# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys
import platform


class Rapidjson(CMakePackage):
    """A fast JSON parser/generator for C++ with both SAX/DOM style API"""

    homepage = "http://rapidjson.org"
    url = "https://github.com/Tencent/rapidjson/archive/v1.1.0.tar.gz"

    version(
        '1.0.2', sha256='c3711ed2b3c76a5565ee9f0128bb4ec6753dbcc23450b713842df8f236d08666')
    version(
        '1.0.1', sha256='a9003ad5c6384896ed4fd1f4a42af108e88e1b582261766df32d717ba744ee73')
    version(
        '1.0.0', sha256='4189b32b9c285f34b37ffe4c0fd5627c1e59c2444daacffe5a96fdfbf08d139b')

    # released versions compile with -Werror and fail with gcc-7
    # branch-fall-through warnings
    patch('0001-turn-off-Werror.patch', when='@:2020 %gcc@7')

    patch('arm.patch', when='@1.1.0 target=aarch64: %gcc@:5.9')

    # Not correspond to define '-march=native' with Fujitsu compiler.
    patch('remove_march.patch', when='%fj')

    if sys.platform == 'darwin' and platform.machine() == 'arm64':
        patch('darwin-arm64.patch', when='@2020:')

    if sys.platform == 'darwin':
        version('2020.01.04', sha256='7021c782e4b78391320efabb4d35554e406c1a2c6255c2dfc01089b38398c042',
                url='https://github.com/Tencent/rapidjson/tarball/585042c02ba6350e10fc43df8beee1bc097f4c5f', preferred=True)
    else:
        version('1.1.0', sha256='bf7ced29704a1e696fbccf2a2b4ea068e7774fa37f6d7dd4039d0787f8bed98e', preferred=True)

    def cmake_args(self):
        if sys.platform == 'darwin' and platform.machine == 'arm64':
            return ['-DRAPIDJSON_ENABLE_INSTRUMENTATION_OPT=OFF']
        return []
