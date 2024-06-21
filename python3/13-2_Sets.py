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

"""


#  for set() : no order

# Set - Method 2: Declaration with fill-in items

# the set is initialized here
set_two = set((28, True, 2.718281828, "Helium"))
print("type(set_two) = ", type(set_two))

# the set is initialized here
set_three = set([28, True, 2.718281828, "Helium"])
print("type(set_three) = ", type(set_two))

# the set is initialized here
set_four = set({28, True, 2.718281828, "Helium"})
print("type(set_four) = ", type(set_two))

print('set_two =', set_two, '\n')

print(help(set_two.clear), '\n')

print('set_two_cleared =', set_two.clear(), '\n\n Voilà')
