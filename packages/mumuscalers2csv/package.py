# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Mumuscalers2csv(CMakePackage):
    """A conversion utility for Fnorm values."""

    homepage = "https://www.example.com"
    git      = "https://github.com/nantes-m2-rps-exp/mumuscalers2csv.git"
    url      = "https://github.com/nantes-m2-rps-exp/mumuscalers2csv/archive/refs/tags/1.0.0.tar.gz"

    version("master",branch="master")
    version('1.0.0', sha256='cf3e862661679914b29bb8a35f29de5cee0aa21dc33a32625c95c672b837b11a')

    depends_on('aliphysics-lite@1.1.2:')
    depends_on('boost')
    depends_on('fmt')
    depends_on('root')
