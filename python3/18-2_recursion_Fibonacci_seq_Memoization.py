# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


"""
- 3 : Memoization for optimizations

"""

# (2): Fibonacci sequence version 2: using Memoization explicitly

fibonacci_cache = {}


def fibonacci_2(n):
    # if the value is already cached then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_2(n-1) + fibonacci_2(n-2)

    # cache the value in the fibonacci_cache dictionary, then return it
    fibonacci_cache[n] = value

    return value


# test
for n in range(1, 101):
    print(f"fibonacci_2({n}) = {fibonacci_2(n)}")


print("fibonacci_cache = ", fibonacci_cache)
