# bin/bash !
# Daniel OUATTARA
# 02 03 2020
#

"""
Python Date storage:
 > Set
 > List
 > Tuples
 > Dictionary


 Union and intersection of 2 sets
"""

#  integer from 1 - 10:

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 10])

print('odds UNION evens =', odds.union(evens), '\n')
print('evens UNION odds =', evens.union(odds), '\n')
print('odds =', odds, '\n')
print('evens = ', evens, '\n')
print('odds INTERSECTION primes =', odds.intersection(primes), '\n')
print('evens INTERSECTION primes =', evens.intersection(primes), '\n')

print('evens INTERSECTION odds =', evens.intersection(odds), '\n')

print('primes UNION composites = ', primes.union(composites), '\n')


print('2 in primes: ',  2 in primes, '\n')  # True
print('6 in odds: ', 6 in odds, '\n')  # False
print('9 not in evens: ', 9 not in evens, '\n')  # True

print(dir(primes), '\n')