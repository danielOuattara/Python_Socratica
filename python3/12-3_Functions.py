# !bin/bash
# Daniel OUATTARA
# 24 02 2020
#

import math

"""
Functions
"""


# with Keyword argument  feet = 0 , etc ...

def convert_to_centimeters(feet=0, inches=0):
    """Converts inches and/or feet to centimeters"""
    inches_to_centimeters = inches * 2.54
    feet_to_centimeters = feet * 12 * 2.54
    return inches_to_centimeters + feet_to_centimeters


print(convert_to_centimeters(feet=1))
print(convert_to_centimeters(inches=1))
print(convert_to_centimeters(1, 0))
print(convert_to_centimeters(inches=1, feet=1))
print(convert_to_centimeters(feet=5, inches=10))
print(convert_to_centimeters(5, 10))


print("Keyword argument in functions")
'''  
def g(x = 0, y ):
    return x + y
This cause an error: 

--> Keyword argument come last in the definition
'''


def g(y, x=0):
    return x + y


print(g(5))  # 5 + 0 = 5
print(g(5, x=4))  # 5 + 4 = 11
print(g(5, 4))  # 5 + 4 = 11
