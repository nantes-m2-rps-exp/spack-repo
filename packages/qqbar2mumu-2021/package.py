# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class Qqbar2mumu2021(BundlePackage):
    """Bundle for QQBar2MuMu project - 2021 edition."""

    homepage = "https://github.com/nantes-m2-rps-exp/qqbar2mumu-2021"

    version('1.0.0')

    depends_on("mchtracking")
    depends_on("py-mchgeo")
    depends_on("py-numpy")
    depends_on("py-pandas")
    depends_on("py-jupyterlab")
    depends_on("py-vector")
    depends_on("py-hist")
    depends_on("py-uproot")
    depends_on("py-awkward")
    depends_on("py-matplotlib")
    depends_on("py-plotly")

