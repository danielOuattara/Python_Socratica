# !bin/bash
# Daniel OUATTARA
# 28 06 2024

import unittest
from math import pi


print(help(unittest))

"""Write a function to compute the area of a circle"""


def circle_area_v1(r):
    return pi * r**2


# Manual Test

radii = [2, 0, -3, 2+5j, True, "radius"]

for r in radii:
    A = circle_area_v1(r)
    print(f'Area of circle with r = {r} is {A}')


"""
Naming Convention #1
---------------------

/circles.py
/ellipses.py
/hyperbolas.py
/polygons.py
/test_circles.py
/test_ellipses.py
/test_hyperbolas.py
/test_polygons.py


Naming Convention #2
---------------------

/circles.py
/circles_test.py
/ellipses.py
/ellipses_test.py
/hyperbolas.py
/hyperbolas_test.py
/polygons.py
/polygons_test.py

"""
