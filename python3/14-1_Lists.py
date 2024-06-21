# !bin/bash
# Daniel OUATTARA
# 02 03 2020
#

"""
Python Date storage:
 > Set
 > List
 > Tuples
 > Dictionary

 Lists:
"""
#  Methods for creating lists:
# 1. list contractor: list()
# 2. use brackets []

primes = [2, 3, 5, 7, 11, 13]
print('\nprimes =', primes, '\n')
print('primes_length = ', len(primes), '\n')
print(help(primes.append), '\n')

primes.append(17)
primes.append(19)
print('primes =', primes)

print('primes_length = ', len(primes))
print('prime[0] = ', primes[0])
print('prime[1] = ', primes[1])
print('prime[2] = ', primes[2])
print('prime[3] = ', primes[3])
print('prime[-1] = ', primes[-1])
print('prime[-2] = ', primes[-2])

# Slicing

print('primes[2:5] =', primes[2:5])
print('primes[0 :6] =', primes[0:6], '\n')

example = [128, True, 'Alpha', 1.732, [64, False], 56]
print('example =', example)

rolls = [4, 7, 2, 14, 7, 4]  # duplicated items all owed
print('rolls =', rolls)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print('letters =', letters)
print('numbers =', numbers)

numbers_letters = numbers + letters
letters_numbers = letters + numbers

print(numbers_letters)
print(letters_numbers)

print(numbers + letters)  # concatenation
print(letters + numbers)  # order counts

print((letters.append("Hello")))
print((letters.append(["Hello", "one", "two"])))

print('numbers =', numbers)
print('letters =', letters)

print('letters_reversed =', letters.reverse())
#   help(numbers)  # To see all the method related to list

#  help(list.reverse)
numbers_letters.reverse()
print(numbers_letters)
print(80 * '=')
print(80 * '=')
list_zero = list()  # Initialized
print(dir(list_zero))

print(80 * '=')
print(80 * '=')
print(help(list_zero))

print('=-' * 40)

print(help(list_zero.append))
