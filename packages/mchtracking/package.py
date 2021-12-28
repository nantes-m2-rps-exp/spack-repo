# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os

class Mchtracking(CMakePackage):
    """Lite version of Alice MCH Tracking library."""

    homepage = "https://github.com/nantes-m2-rps-exp/mchtracking.git"
    git      = "https://github.com/nantes-m2-rps-exp/mchtracking.git"
    url      = "https://github.com/nantes-m2-rps-exp/mchtracking/archive/refs/tags/0.1.0.tar.gz"
    
    variant('python',default=True,description='build python bindings')

    generator = "Ninja"

    version('master',branch='master')
    version('0.1.1', sha256='ff3862550460a3d16f546ff0de13e11fd4ce2c7e095b2987633d362afac5ee61')
    version('0.1.0', sha256='b2e3dc1657074efe5e9d24cbfd70ac3b471809a9e07d8347601283511ea76dc2')

    depends_on('boost',when='@:0.1.0')
    depends_on('fairlogger')
    depends_on('fmt')
    depends_on('root')

    depends_on('ninja',type='build')

    with when('+python'):
        extends('python')
        depends_on('py-pybind11',type='build')
        depends_on('py-pytest',type='build')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        args.append(self.define_from_variant("BUILD_PYTHON_BINDINGS","python"))
        return args

    def setup_build_environment(self,env):
        env.set('O2_ROOT',os.path.join(self.build_directory,'stage'))
        if '+python' in self.spec:
            env.prepend_path('PYTHONPATH',os.path.join(self.build_directory,'stage/lib'))

    def setup_run_environment(self,env):
        env.set('O2_ROOT',self.prefix)
        env.append_path('ROOT_INCLUDE_PATH',os.path.join(self.prefix,'include'))
