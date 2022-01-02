# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyDecaylanguage(PythonPackage):
    """DecayLanguage: describe, manipulate and convert particle decays."""

    pypi     = "DecayLanguage/DecayLanguage-0.13.0.tar.gz"


    version('0.13.0', sha256='eaa68b796f01475186227a353fa94099da5a757d188f855e7cf0f249bcb82c6d')

    depends_on('py-setuptools', type='build')
    depends_on('py-attrs@19.2:')
    depends_on('py-deprecated')
    depends_on('py-graphviz')
    depends_on('py-lark-parser@0.11:')
    depends_on('py-numpy@1.12:')
    depends_on('py-pandas@0.22:')
    depends_on('py-particle@0.16:')
    depends_on('py-plumbum@1.6.9:')
    depends_on('py-importlib-resources@2:')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
