# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPlumbum(PythonPackage):
    """Shell Combinators and More."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://plumbum.readthedocs.io/en/latest/"
    pypi     = "plumbum/plumbum-1.7.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.7.2', sha256='0d1bf908076bbd0484d16412479cb97d6843069ee19f99e267e11dd980040523')

    depends_on('py-setuptools',  type=('build'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
