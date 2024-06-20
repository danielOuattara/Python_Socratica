# Daniel OUATTARA
# 02 03 2020
# Socratica-Python3.x

"""
If - Then - Else

"""

# Nature of a triangle by its 3 given length:

a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c:"))

if a == b and a == c:
    print("this triangle is equilateral")
elif a == b and a != c:
    print("this triangle is isosceles")
else:
    print("this triangle is scalene")
