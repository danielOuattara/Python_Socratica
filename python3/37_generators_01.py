# Daniel OUATTARA
# 01 07 2024


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
  'yield' to return a series of values, one at a time, pausing after 
  each yield and resuming from where it left off when called again.

- Generators are useful for generating large sequences of values on 
  the fly without storing them in memory all at once.


  VS


Iterators:
----------

- loops over objects in memory

"""


def f():
    return 1
    return 2
    return 3


print(f())   # 1


def g():

    yield 1
    yield 2
    yield 3


print(g())  # <generator object g at 0x7f56fa5b8b40>

# g() return a generator object, that act like iterators;
# so we can loop over it


for item in g():
    print(item)

# 1
# 2
# 3
