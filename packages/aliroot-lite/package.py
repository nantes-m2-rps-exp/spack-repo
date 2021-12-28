# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class AlirootLite(CMakePackage):
    """A Lite version of AliRoot"""

    homepage = "https://www.example.com"
    git      = "https://github.com/nantes-m2-rps-exp/aliroot-lite.git"
    url      = "https://github.com/nantes-m2-rps-exp/aliroot-lite/archive/refs/tags/1.1.0.tar.gz"

    version("master",branch="master")
    version('1.1.0', sha256='e1255ccee8db50b9450d38dc48188cf76e07ce6c06195dbd79429e505056b227')

    depends_on('vmc@1-1-p1:')
    depends_on('alice-grid-utils')
    depends_on('jalien-root')
