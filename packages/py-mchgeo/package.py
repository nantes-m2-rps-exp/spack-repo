# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyMchgeo(PythonPackage):
    """Basic Alice MCH Geometry."""

    homepage = "https://github.com/nantes-m2-rps-exp/mchgeo.git"
    git      = "https://github.com/nantes-m2-rps-exp/mchgeo.git"
    url = "https://github.com/nantes-m2-rps-exp/mchgeo/archive/refs/tags/0.1.2.tar.gz" 

    maintainers = ['aphecetche']

    version('master')
    version('0.1.2', sha256='4162f7d4360e6df559f844084861b0d81d336ca9aed6858e0a6af2d62778f6e5')

    depends_on('py-setuptools@42:',type='build')
    depends_on('py-importlib-resources',type='build')

    @run_before('build')
    def create_setup(self):
        with open('setup.py','w') as f:
            f.write("from setuptools import setup\n")
            f.write("setup()")
            f.close()

