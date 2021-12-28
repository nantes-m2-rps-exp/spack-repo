# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os

class Mchmapping(CMakePackage):
    """External version of Alice O2 MCH mapping library."""

    homepage = "https://github.com/nantes-m2-rps-exp/mchmapping.git"
    git      = "https://github.com/nantes-m2-rps-exp/mchmapping.git"
    url      = "https://github.com/nantes-m2-rps-exp/mchmapping/archive/refs/tags/0.1.0.tar.gz"
    
    variant('python',default=True,description='build python bindings')

    generator = "Ninja"

    version('master',branch='master')

    depends_on('boost')
    depends_on('fmt')
    depends_on('root')
    depends_on('cppgsl')

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
        if '+python' in self.spec:
            env.prepend_path('PYTHONPATH',os.path.join(self.build_directory,'stage/lib'))

