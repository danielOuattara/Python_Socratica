# !bin/bash
# Daniel OUATTARA
# 02 03 2020
# Socratica-Python3.x

import sys  # bring a library of system functions


'''Numbers in Python 3:
=======================

-> 4 type of numbers in Python 2: 
-> 3 types of numbers in Python 3

'''

# int, float, complex

#  int type
#  ==========

a = 496
type(a)  # <int>
print(type(a))  # <int>
print(a)
limit = sys.maxsize
print(limit)  # 9_223_372_036_854_775_807
print(type(limit))  # <int>

b = 9223372036854775808
print(type(b))

#  floats type
#  ===========

e = 2.718281828
type(e)
print('e = ', e)
print(type(e))


#  Complex type
#  ==============

z = 2 - 6.1j
type(z)
print(type(z))

print(z.real)
print(z.imag)




