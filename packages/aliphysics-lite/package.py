# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class AliphysicsLite(CMakePackage):
    """A Lite version of Aliphysics"""

    homepage = "https://www.example.com"
    git      = "https://github.com/nantes-m2-rps-exp/aliphysics-lite.git"
    url      = "https://github.com/nantes-m2-rps-exp/aliphysics-lite/archive/refs/tags/1.1.0.tar.gz"

    version("master",branch="master")
    version('1.1.1', sha256='eb9d06fe33c3243ee4f02d61af58b5b7c4d82ba75354ce747f833de2051bcde0')
    version('1.1.0', sha256='028b92cf033ff484fd70812f120cca92fba3ed63ed7db2e10cb3050b971b3590')
    version('1.0.0', sha256='e57a14c0b4e1bba93e11f5a8d774d2050ab9b83625880882615f6206bdee7604')

    depends_on('aliroot-lite@1.1.0:')

    def setup_run_environment(self,env):
      env.set('ALICE_PHYSICS',self.prefix)
      env.append_path('ROOT_INCLUDE_PATH',os.path.join(self.prefix,'include'))

