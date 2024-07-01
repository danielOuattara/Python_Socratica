# Daniel OUATTARA
# 01 07 2024

import itertools
import sys

"""
Generators:
-----------

° Generators allow you to iterate over data without storing 
it in memory all at once, making them powerful for handling 
large datasets.

° Writing generator functions using yield and understanding 
how they maintain state can be tricky.

generators :

- functions that acts like iterators

- generates the element in a loop

- as a on-demand iterable object

generators :

- Generators are a simple way to create iterators using functions.

- Instead of returning a single value, a generator function uses 
  'yield' to return a series of values, one at a time, pausing after each yield and resuming from where it left off when called again.
Generators are useful for generating large sequences of values on the fly without storing them in memory all at once.

VS


Iterators:
----------

- loops over objects in memory


discussion
-----------

List comprehension: [ expression]

Generator Expression: (expression)

"""

# Writing a generator function that will generate
# the square of all positive integers


squares = (x**2 for x in itertools.count(1, 1))

# print(squares)
# print(type(squares))


for x in squares:
    print(x)
    if x > 1_000_000:
        squares.close()


print('sys.getsizeof(squares) = ', sys.getsizeof(squares))


"""
Conclusion: 2 ways to create generators

1- write a function and use 'yield' instead of 'return'

2- use a generator expression

"""
