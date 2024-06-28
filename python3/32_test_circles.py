# !bin/bash
# Daniel OUATTARA
# 28 06 2024

from _32_circles import circle_area
from math import pi
import unittest


""""
python3 -m unittest 32_test_circles
"""


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure radius is only int or float
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, 'Hello')
