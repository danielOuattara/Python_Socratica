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

"""
#  Methods for creating Sets:
#  ----------------------------
#  1. set constructor: set()
#  2. use brackets {}


#  for set() : no order, no duplicate, updatable, removable

# Set - Method 1: Declaration without fill-in any value


set_one = set()  # the set is initialized here
print(dir(set_one))

#  print(help(set_one), '\n')
print(help(set_one.add), '\n')

set_one.add(43)
set_one.add(False)
set_one.add(3.14159)
set_one.add("Thorium")

print("set_one = ", set_one, '\n')

set_one.add(43)  # No duplicate allowed, No Error raised
print("set_one = ", set_one, '\n')

print('set_one_length = ', len(set_one), '\n')

# duplicate set created are remove
set_zero = set({1, 1, 3, 4, "hello", "hello"})
print(set_zero)


print(help(set_one.remove), '\n')  # use remove method to remove

set_one.remove(43)  # 43 is member of set set_one
print("set_one = ", set_one, '\n')  # 43 is member of set set_one
print('set_one_length = ', len(set_one), '\n')

# set_one.remove(43)  # 43 is member of set set_one
# print("set_one = ", set_one, '\n')  # 43 is member of set set_one
# print('set_one_length = ', len(set_one), '\n')

print(help(set_one.discard), '\n')  # No error if the item is not in the set
set_one.discard(50)  # Nothing happens
print(set_one, '\n')
