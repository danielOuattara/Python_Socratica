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


 Tuple VS List:
"""
import sys
import timeit

# ---> Identical characteristics between Tuples and Lists

#  List example:
prime_numbers = [2, 3, 5, 7, 11, 13, 17]
print('\nprime_numbers =', prime_numbers)

#  Tuple example:
perfect_squares = (1, 4, 9, 16, 25, 36)
print('perfect_squares =', perfect_squares, '\n')

print('-' * 40)

#  Display lengths:
print("primes_#_length = ", len(prime_numbers))
print("squares_#_length = ", len(perfect_squares))

# Iterate over both sequences
for p in prime_numbers:
    print('prime:', p)

print('-' * 40)
for n in perfect_squares:
    print('squares:', n)

# ---> Opposite characteristics between Tuples and Lists

#  List of methods available for each object:
print('-' * 40)
print("Methods available for: List")
print(dir(list))  # equivalent to:: print(dir(prime_numbers))

#  because prime_numbers is a list
print(200 * '---')
print("Methods available for: Tuple")
print(dir(tuple))  # equivalent to:: print(dir(perfect_squares)
#  because perfect_squares is a tuple
#  Conclusion: List occupy more memory than tuples

print(200 * '---')

#  print('Print of dir(sys):')
#  print(dir(sys))

print(help(sys.getsizeof))

#  Compare the size of a List and Tuple
#  containing the same exact data

list_1 = [1, 2, 3, 4, "argent", "b", "c", 3.14159, 2.12345678, True]
tuple_1 = (1, 2, 3, 4, "argent", "b", "c", 3.14159, 2.12345678, True)

print('size_list_1 =', sys.getsizeof(list_1), 'bytes')
print('size_tuple_1 =', sys.getsizeof(tuple_1), 'bytes')

'''
Lists:              Tuples:
------              -------

 > Add data      | > cannot be changed
 > Remove data   | > "Immutable"  
 > Change data   | > Made quickly and use less memory

'''

#  Check for time:

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=int(1e+7))
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=int(1e+7))

print("List time: ", list_test)
print("Tuple time: ", tuple_test)
