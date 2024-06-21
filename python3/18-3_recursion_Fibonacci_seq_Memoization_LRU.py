# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


"""

- 3 : Memoization LRU for optimizations + input checks

"""


# (1): Fibonacci sequence:


from functools import lru_cache

#  LRU Least Recently Used Cache


@lru_cache(maxsize=1000)
def fibonacci_3(n):
    #  check input for positive integer

    if type(n) != int:
        raise TypeError("'n' value must be an integer")
    if n < 1:
        raise ValueError("'n' value must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_3(n-1) + fibonacci_3(n-2)


#  test
# for n in range(1, 501):
    # print(f"fibonacci_3({n}) = {fibonacci_3(n)}")

for n in range(1, 101):
    print(fibonacci_3(n+1) / fibonacci_3(n))

# -------------------------------------------------------------
