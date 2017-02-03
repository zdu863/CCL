#!/usr/bin/env python

from distutils.core import *
from distutils import sysconfig
import os.path

# Get numpy include directory (works across versions)
import numpy
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

LIBCCL_LIBRARY_PATH = "/home/phil/jpl/software/lib/"

# CCL extension module
_ccllib = Extension(
            "_ccllib",
               ["pyccl/ccl.i",],
               libraries = ['m', 'gsl', 'gslcblas', 'gomp', 'ccl'],
               library_dirs = [LIBCCL_LIBRARY_PATH,],
               runtime_library_dirs = [LIBCCL_LIBRARY_PATH,],
               include_dirs = [numpy_include, "include/", "class/include"],
               extra_compile_args=['-O4', '-fopenmp',],
               swig_opts=['-threads'],
           )

# CCL setup script
setup(  name         = "pyccl",
        description  = "Library of validated cosmological functions.",
        author       = "LSST DESC",
        version      = "0.1",
        packages     = ['pyccl'],
        ext_modules  = [_ccllib,],
        )

