# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class Teachers(BundlePackage):
    """Bundle for QQBar2MuMu project - 2022 edition - teachers' version"""

    homepage = "https://github.com/nantes-m2-rps-exp/"

    version('1.0.0')

    depends_on('qqbar2mumu-2022')
    depends_on('mumuscalers2csv') # brings aliroot-lite and aliphysics-lite

