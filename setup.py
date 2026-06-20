"""
setup.py
--------
This file tells Python HOW to build and install our C++ extension module.

It uses setuptools + pybind11 to:
  1. Find the pybind11 headers (so the C++ compiler knows about pybind11).
  2. Compile our C++ source file (src/mymath.cpp) into a shared library.
  3. Package it so "import mymath" works in Python.

To build and install, run:
    pip install .
"""

from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

# ============================================================
# Define the C++ extension module
# ============================================================
ext_modules = [
    Pybind11Extension(
        # The name of the Python module (what you write after "import")
        "mymath",
        # List of C++ source files to compile
        ["src/mymath.cpp"],
    ),
]

# ============================================================
# Call setup() to configure the package
# ============================================================
setup(
    name="mymath",                          # Package name on PyPI / pip
    version="0.1.0",                        # Version number
    author="Mussa Khan",                     # Your name
    author_email="musagithub1@users.noreply.github.com",
    description="A simple math library written in C++ with pybind11",
    ext_modules=ext_modules,                # Our C++ extension(s)
    cmdclass={"build_ext": build_ext},      # Use pybind11's build command
    python_requires=">=3.7",                # Minimum Python version
)
