# !bin/bash
# Daniel OUATTARA
# 28 06 2024

from math import pi


def circle_area(r):
    """Write a function to compute the area of a circle"""

    if type(r) not in [int, float]:
        raise TypeError('radius must be an integer or a float')

    if r < 0:
        raise ValueError('radius must be positive')

    return pi * r**2
