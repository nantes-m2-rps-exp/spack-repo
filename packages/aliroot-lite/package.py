# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class AlirootLite(CMakePackage):
    """A Lite version of AliRoot"""

    homepage = "https://www.example.com"
    git      = "https://github.com/nantes-m2-rps-exp/aliroot-lite.git"
    url      = "https://github.com/nantes-m2-rps-exp/aliroot-lite/archive/refs/heads/master.tar.gz"

    version("master")

    depends_on('vmc@1-1-p1:')
    depends_on('alice-grid-utils')
    depends_on('jalien-root')
