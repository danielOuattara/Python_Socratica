# !bin/bash
# Daniel OUATTARA
# 25 02 2020
#

import math

""" Functions  """


def sphere_volume(radius: float):
    """Returns the volume of a sphere, given a radius """
    calc = 4.0 / 3.0 * math.pi * radius ** 3
    return calc


print(sphere_volume(5.0))

help(sphere_volume)


def triangle_area(base: float, height: float):
    """Returns the area of a triangle, given:
       its base length 'b' and its height 'h'  """
    return 0.5 * height * base


print(triangle_area(12, 5))
