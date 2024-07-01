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
  'yield' to return a series of values, one at a time, pausing after each yield and resuming from where it left off when called again.
Generators are useful for generating large sequences of values on the fly without storing them in memory all at once.

VS


Iterators:
----------

- loops over objects in memory

"""

# Write a function that yields each lower case letter in the english alphabet.
# or generate the lower case english letters


import math
import itertools
import string


# for item in dir(string):
#     print(item)

"""
Formatter
Template
_ChainMap
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_re
_sentinel_dict
_string
ascii_letters
ascii_lowercase
ascii_uppercase
capwords
digits
hexdigits
octdigits
printable
punctuation
whitespace
"""


def letters():
    for c in string.ascii_lowercase:
        yield c


for letter in letters():
    print(letter)


"""
discussion
-----------

- a function that uses 'yield' instead of return  is a generator function
 or simply a generator

def function():
    yield <expression>

-----

- when a generator calls a 'yield', it momentarily
  control back to the code looping over the generators values

def genX():
    # Do something cool
    yield <value>


for event in genX():
    # Do something with event


"""
# Writing a generator function that yields all the prime numbers


def prime_numbers():
    """other than 2 , all prime number are odd numbers"""
    # handle the case the 1st prime number
    yield 2

    # cache for prime numbers
    prime_cache = [2]

    # next: loop over all positive odd number starting with 3:
    for n in itertools.count(3, 2):
        is_prime = True
        # check if any prime number in cache divides n
        for p in prime_cache:
            if n % p == 0:  #  p divides n evenly
                is_prime = False
                break

        # Is it prime ?
        if is_prime:
            prime_cache.append(n)
            yield n


# for p in prime_numbers():
#     print(p)
#     if p > 1_000:
#         break


# -------------------------------------------------------------

# Optimized

def prime_numbers_2():
    """Yield prime numbers indefinitely."""
    yield 2  # First prime number
    prime_cache = [2]  # Cache of discovered prime numbers

    # Loop over all positive odd numbers starting with 3
    for n in itertools.count(3, 2):
        is_prime = True
        sqrt_n = math.isqrt(n)  # Efficient square root

        # Check divisibility only with primes up to sqrt(n)
        for p in prime_cache:
            if p > sqrt_n:
                break
            if n % p == 0:
                is_prime = False
                break

        if is_prime:
            prime_cache.append(n)
            yield n


# Usage example
for p in prime_numbers():
    print(p)
    if p > 1_000_000:
        break
