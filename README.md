[![HitCount](http://hits.dwyl.io/mitgobla/TopograPy.svg)](http://hits.dwyl.io/mitgobla/TopograPy)
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

## Example Usage
```python
import topograpy

cross_section = topograpy.CrossSection()
graph = topograpy.SectionCalculation()

topograph = cross_section.calculate("height_map.png", graph)
coordinates = cross_section.return_coordinates()
image_size = coordinates[2] # Tuple of image x and y size
heights = graph.return_darkness() # The height of each line based on height % of image
```

To get the darkness (height factor) for a specific pixel:
```python
>>> heights[x_coordinate][y_coordinate]
>>> heights[0][0]
25
# The higher the number, the 'taller' the pixel on the height map
```

Generator for creating two sets of coordinates to generate a line.
```python
generated_coordinates = [[], []]
for x_coord in range(image_size[0]):
    for y_coord in range(image_size[1]):
        generated_coordinates[0].append((x_coord, heights[x_coord][y_coord], y_coord)
        generated_coordinates[1].append((x_coord, 0, y_coord))
```
This will generate a list with two lists `xyz1` and `xyz2` 
```python
>>> generated_coordinates[0][0]
(0, 25, 0)
>>> generated_coordinates[1][0]
(0, 0, 0)
```