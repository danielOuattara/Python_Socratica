# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


""""
Logging
---------

Levels: Debug, Info, Warning, Error, Critical

Application: Quadratic Formula Equations Resolution

ax**2 + bx + c = 0

x1 = (-b - sqrt(b**2 -4ac))/2a 
x2 = (-b + sqrt(b**2 -4ac))/2a 

"""

import logging
from math import sqrt


# for item in dir(logging):
#     print(item)

"""
NOTE: while reading above output, keep in mind:
- uppercase items are constants
- capitalize items are classes
- lowercase items are methods
"""


LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(
    filename="17_quadratic_formula.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode='w'
)

logger = logging.getLogger()  # no name provided for logger


def quadratic_formula(a: float, b: float, c: float):
    """ Return  the solutions to the equation ax**2 + bx + c = 0"""
    logger.info(f"quadratic_formula({a}, {b}, {c})")

    # compute the discriminant:
    logger.debug('# compute the discriminant: ')
    delta = b**2 - 4 * a * c

    if delta < 0:
        logger.warning('# No solution: found delta < 0 ')
        return None
    elif delta == 0:
        logger.debug('# found a unique solution: ')
        root = -b / 2*a
        return root
    else:
        logger.debug('# found 2 distinct solutions: ')
        root1 = (-b - sqrt(delta))/2*a
        root2 = (-b + sqrt(delta))/2*a
        return (root1, root2)


quadratic_formula(1, 0, -1)
quadratic_formula(1, 0, 1)
quadratic_formula(-1, 0, 1)
