# Daniel OUATTARA
# 02 07 2024


"""Decorators in some Python modules
------------------------------------ """

#  In Python, function are First Class Citizens that can be nested


import functools
import time


# for item in dir(functools):
#     print(item)


"""
# functools elements
# -------------------

GenericAlias
RLock
WRAPPER_ASSIGNMENTS
WRAPPER_UPDATES
_CacheInfo
_HashedSeq
_NOT_FOUND
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_c3_merge
_c3_mro
_compose_mro
_convert
_find_impl
_ge_from_gt
_ge_from_le
_ge_from_lt
_gt_from_ge
_gt_from_le
_gt_from_lt
_initial_missing
_le_from_ge
_le_from_gt
_le_from_lt
_lru_cache_wrapper
_lt_from_ge
_lt_from_gt
_lt_from_le
_make_key
_unwrap_partial
cache    # <<< decorator
cached_property
cmp_to_key
get_cache_token
lru_cache
namedtuple
partial
partialmethod
recursive_repr
reduce
singledispatch
singledispatchmethod
total_ordering
update_wrapper
wraps    # <<< decorator
"""


""" Example using the 2 decorators of the above (wraps, cache) """
# Example using the 'wraps' decorator


def alpha(*args, **kwargs):
    """A function for viewing arguments"""
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


alpha('a', 2, None, x=7, y=11, z=28)

print(alpha.__name__)
print(alpha.__doc__)

print('----------------------------------------------------')

# a do nothing decorator


def do_nothing_2(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper


@do_nothing_2
def alpha_2(*args, **kwargs):
    """A function for viewing arguments"""
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


print(alpha_2.__name__)
print(alpha_2.__doc__)

# moral story: name and doc stream are ... lost !

print('----------------------------------------------------')

#  solution to previous loss: using wraps from functools


def do_nothing_3(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper


@do_nothing_3
def alpha_3(*args, **kwargs):
    """A function for viewing arguments"""
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


print(alpha_3.__name__)
print(alpha_3.__doc__)

"""
IMPORTANT: above, functools.wraps() accepts an argument
It possible to design decorators that accepts arguments
to modify the behavior of the decorator

See below

"""

# --------------------------------------------------------
# Example using the 'cache' decorator on a Fibonacci suit
# The cache decorator provide a function with memoization

#  Memoization :: = cache a function calls for future reuses


# --------------

# re-define a timer calculator

def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        print(f'delta = {stop_time - start_time}\n')
        return result

    return wrapper


# manually optimized example for Fibonacci
fibonacci_cache = {}


def fibonacci_1(n):

    # input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError(f'{n} is not a positive integer')

    # if the value is already cached then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci_1(n-1) + fibonacci_1(n-2)

    # cache the value in the fibonacci_cache dictionary, then return it
    fibonacci_cache[n] = value

    return value


# test
for n in range(1, 10):
    print(f"fibonacci_1({n}) = {fibonacci_1(n)}")

# print("fibonacci_cache = ", fibonacci_cache)


print('----------------------------------------------------------')


def fibonacci_2(n):
    # input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError(f'{n} is not a positive integer')

    # compute the nth term
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_2(n-1) + fibonacci_2(n-2)


# Test for : fibonacci_2
for n in range(1, 10):
    print(f'fibonacci_2({n}) = {fibonacci_2(n)}')

"""
An issue if you decorate fibonacci_2() with @timer: delta time too much printed

Solution below: use a global wrapper
"""

print('----------------------------------------------------------')


def fibonacci_3(n):
    # input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError(f'{n} is not a positive integer')

    # compute the nth term
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_3(n-1) + fibonacci_3(n-2)


@timer
def global_for_fibonacci_3(n):
    return fibonacci_3(n)


# Test for : fibonacci_3
for n in range(1, 10):
    print(f'global_for_fibonacci_3({n}) = {global_for_fibonacci_3(n)}')

""" 
An issue still arises: computing time... excessive

SOLUTION: Using 'functools.cache' to memoize
"""

print('----------------------------------------------------------')


@functools.cache
def fibonacci_4(n):
    # input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError(f'{n} is not a positive integer')

    # compute the nth term
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_4(n-1) + fibonacci_4(n-2)


@timer
def global_for_fibonacci_4(n):
    return fibonacci_4(n)


# Test for : fibonacci_4
for n in range(1, 100):
    print(f'global_for_fibonacci_4({n}) = {global_for_fibonacci_4(n)}')
