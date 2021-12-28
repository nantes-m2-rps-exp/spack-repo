# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Aod2tree(CMakePackage):
    """AOD to Tree converter."""

    homepage = "https://www.example.com"
    git      = "https://github.com/nantes-m2-rps-exp/aod2tree.git"
    url      = "https://github.com/nantes-m2-rps-exp/aod2tree/archive/refs/tags/1.0.0.tar.gz"

    version("master",branch="master")

    depends_on('aliphysics-lite@1.1.1:')
