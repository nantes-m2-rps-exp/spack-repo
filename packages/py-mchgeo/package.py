# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyMchgeo(PythonPackage):
    """Basic Alice MCH Geometry."""

    homepage = "https://github.com/nantes-m2-rps-exp/mchgeo.git"
    git      = "https://github.com/nantes-m2-rps-exp/mchgeo.git"
    url = "https://github.com/nantes-m2-rps-exp/mchgeo/archive/refs/tags/0.1.3.tar.gz" 

    maintainers = ['aphecetche']

    version('master')
    version('0.1.3', sha256='094235c4d4e08e9849c056967cfcaa348ff74a1595845c3b61bace9ec5595399')

    depends_on('py-setuptools@42:',type='build')
    depends_on('py-importlib-resources',type='build')

    @run_before('build')
    def create_setup(self):
        with open('setup.py','w') as f:
            f.write("from setuptools import setup\n")
            f.write("setup()")
            f.close()

