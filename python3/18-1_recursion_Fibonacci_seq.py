# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


"""
- 1 : Fibonacci sequence
- 2 : Recursion is required for Fibonacci sequence
- 3 : Memoization for optimizations


- first terms sequence : 1, 1, 2, 3, 5, 8, 13, 21

1 + 1  = 2
1 + 2  = 3
2 + 3  = 5
3 + 5  = 8
5 + 8  = 13
8 + 13 = 21
...etc

- Goal: Write a function that returns the nth term of the Fibonacci sequence

- Requirements: Fast , Clean, Solid

"""


# (1): Fibonacci sequence:

def fibonacci_1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_1(n-1) + fibonacci_1(n-2)


#  test
for n in range(1, 51):
    print(f"fibonacci_1({n}) = {fibonacci_1(n)}")
