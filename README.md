# TopograPy
A Height Map Coordinate Generator in Python.
Windows Only.
Please note: this program is being completely re-programmed to add more coordinate generation options to suit generation of height maps in different forms. As of the current version, it only supports being generated onto a 2D canvas that can't be rotated; I am planning on changing this in the future.
## Installing Requirements
Pillow is the only requirement for this module and it is used for reading images. To install, use: 
```
pip install pillow
```
## Setup
ToporaPy is not available on PyPI yet, but you can still install the master branch through `pip` with the following command:
```
pip install -e git+https://github.com/mitgobla/TopograPy.git@master#egg=topograpy
```
Alternatively, you can get future versions that have not been release to the `master` branch by using the following:
```
pip install -e git+https://github.com/mitgobla/TopograPy.git@future#egg=topograpy
```
