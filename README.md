# Titrafit
## Prerequisites
The following Python 3 packages must be installed to use Titrafit:
* Matplotlib
* NumPy
* PySide2
* SciPy

## Building tfast
Titrafit provides a C++ implementation of the fit function which greatly deduces the time required for the computation.
For the compilation of the corresponding module, the following software is required:
* [Pybind11](https://github.com/pybind/pybind11) headers (available via `pip` and some Linux package managers)
* Python 3 headers (usually bundled with Python 3, in separate package `libpython3-dev` on Debian/Ubuntu)
* A C++14-capable compiler such as g++, Clang oder MSVC

On Linux, tfast can be compiled with the following command:
```
g++ -std=c++14 -O2 -fPIC -shared -o tfast.so `python3 -m pybind11 --includes` tfast.cpp
```

On Windows, the compilation command is as follows:
```
cl /O2 /LD /I <C:\path\to\Python\>include tfast.cpp /link <C:\path\to\Python>\libs\python3<x>.lib /OUT:tfast.pyd
```

## Editing the UI files
The user interface is defined in the `.ui` files which can be edited with Qt Designer. From these,
the corresponding `ui_*.py` files are generated with `pyside2-uic`, e.g.:
```
pyside2-uic inputform.ui > ui_inputform.py
```
The resulting `ui_*.py` files are included in the Git repository so Titrafit can be run right after cloning the repository,
without any additional build steps.
