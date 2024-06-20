# bin/bash !
# Daniel OUATTARA
# 24 02 2020
# Socratica-Python3.x

import sys  # bring a library of system functions

'''Arithmetic in Python 3:
=======================
 
 Numbers: int, float, complex
 Operations: + - * /  //
'''

x = 28  # int
x_2 = 28.0  # float
y = 28.2350  # float
y_2 = float(28)  # float
z = 2.14 + 3.15j

pi = 3.14  # float
int(pi)  # = 3 int

float(28)  # 28 --> 28.0  # float() = float constructor
int(28.0)  # 28.2350 --> 28  # int() = int constructor
complex(y)  # possible
complex(x)  # possible
# float(z)  # impossible
# int(z)  # impossible


"""Basic operations"""

a = 2  # int
b = 6.0  # float
c = 12 + 0j  # complex number

# Rule: Widen numbers, so they're the same type
# ==============================================

# Addition :
print(a + b)  # int + float = 8.0  float

# Subtraction:
print(b - a)  # float - int = 4.0  float

# Multiplication:
print(a * 7)  # int * int = 14 int

# Division:
print(c / b)  # complex / float = 2+ 0j  complex

z = 1.45

z = 1.45 + 0j  # hand made complex

complex(z)  # 1.45 + 0j , type complex, using the complex constructor

print(16 / 5)  # 3.2

print(20 / 5)  # 4.0

print(16 % 5)  # 1

print(16 // 5)  # 3 is the quotient of 16/5
