# !bin/bash
# Daniel OUATTARA
# 24 06 2024

""" 

- Prime numbers: only divisible by itself and by 1

- Composite numbers: Can be factored into smaller integers

- Find prime numbers

- Write a series of functions to efficiently find prime numbers


"""


import math
import time

# ==============  is_prime_v1 =================


def is_prime_v1(n: int):
    """ Return True if 'n' is a prime number. False otherwise """

    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


# -------- Test is_prime_v1 --------

# for n in range(1, 21):
#     print(n, is_prime_v1(n))

# -------- Test is_prime_v1 for speed
# t0 = time.time()
# for n in range(1, 100_000):
#     is_prime_v1(n)
# t1 = time.time()

# print(f'\nTime required: {t1 -t0}\n')
# Time required: 23.535857439041138


# ==============  is_prime_v2 =================


def is_prime_v2(n: int):
    """ 
    Return True if 'n' is a prime number. False otherwise
    Reduce the number of divisor we check 

    """

    if n == 1:
        return False

    for d in range(2, int(math.sqrt(n) + 1)):
        if n % d == 0:
            return False
    return True


# -------- Test is_prime_v2 --------

# for n in range(1, 21):
#     print(n, is_prime_v2(n))


# -------- Test is_prime_v2 for speed
t0 = time.time()
for n in range(1, 100_000):
    is_prime_v2(n)
t1 = time.time()

print(f'\nTime required: {t1 -t0}\n')
# Time required: 0.13557004928588867

# ==============  is_prime_v2 =================


def is_prime_v3(n: int):
    """ 
    - Return True if 'n' is a prime number. False otherwise
    - Reduce the number of divisor we check &
    - Test if n is even &
    - Test only for odd divisors: if the input is odd, it is waist to check for even divisors
    """

    if n == 1:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    for d in range(3, int(math.sqrt(n) + 1), 2):
        if n % d == 0:
            return False
    return True


# -------- Test is_prime_v3 --------

for n in range(1, 21):
    print(n, is_prime_v3(n))


# -------- Test is_prime_v3 for speed
t0 = time.time()
for n in range(1, 100_000):
    is_prime_v3(n)
t1 = time.time()

print(f'\nTime required: {t1 -t0}\n')

# Time required: 0.07943892478942871
