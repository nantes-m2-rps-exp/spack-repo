# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os

class Mchtracking(CMakePackage):
    """Lite version of Alice MCH Tracking library and its Python bindings."""

    homepage = "https://www.example.com"
    git      = "https://github.com/nantes-m2-rps-exp/mchtracking.git"
    url      = "https://github.com/nantes-m2-rps-exp/mchtracking/archive/refs/tags/v0.0.1.tar.gz"
    
    extends('python')
    generator = "Ninja"

    version('dev',branch='dev')
    version('0.0.1', sha256='0e9fb4f778417a62170888d558426107f30c64d64634e3799e38f37278c5998d')

    depends_on('boost')
    depends_on('fairlogger')
    depends_on('fmt')
    depends_on('ninja',type='build')
    depends_on('py-pybind11',type='build')
    depends_on('py-pytest',type='build')
    depends_on('root')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        return args

    def setup_build_environment(self,env):
        env.set('O2_ROOT',os.path.join(self.build_directory,'stage'))
        env.prepend_path('PYTHONPATH',os.path.join(self.build_directory,'stage/lib'))

    def setup_run_environment(self,env):
        env.set('O2_ROOT',self.prefix)
        env.append_path('ROOT_INCLUDE_PATH',os.path.join(self.prefix,'include'))
