# Daniel OUATTARA
# 01 07 2024


"""
Iterators Iterables Itertools

In Python if you can loop over something, then that something
is called an iterable

- a sequence = iterable + ordered
- common sequences: lists, tuples, strings, bytes
"""

print('-------------')
# list
for person in ['Cyril Collin', 'Len Klein', 'Mathias Stein', 'Mike Tyson']:
    print(person)

print('-------------')
# tuples
for person in ('Cyril Collin', 'Len Klein', 'Mathias Stein', 'Mike Tyson'):
    print(person)

print('-------------')
# string
for letter in 'Python':
    print(letter)

print('-------------')
# bytes: 97-122 lower case letter
for letter in b'abcdefghijklmnopqrstuvwxyz':
    print(letter)

print('-------------')
# bytes 65-90 uppercase letter
for letter in b'abcdefghijklmnopqrstuvwxyz'.upper():
    print(letter)

print('-------------')
# bytes
for letter in b'Python':
    print(letter)


print('------------- for number: work around')

number = 214253489
digits = [int(digit) for digit in str(number)]
for item in digits:
    print(item)

print('-------------')
for item in digits:
    print(bin(item))


"""  What makes an object iterable ?

Docs:

collections.abc : abstract base classes

ABC           Inherits from      Abstract Methods
----          --------------     ----------------
(...)
Iterable       None               __iter__
Iterator       Iterable           __next__
(...)


container.__iter__() : 
    Return an iterator object

iterator.__next__() : 
    Return the next item from the container.
    If there are no further items to iterate over, 
    raise the StopIteration exception
"""


customers = ('Cyril Collin', 'Len Klein', 'Mathias Stein', 'Mike Tyson')

looper_1 = customers.__iter__()

print(type(looper_1))  # <class 'tuple_iterator'>

try:
    print(looper_1.__next__())
    print(looper_1.__next__())
    print(looper_1.__next__())
    print(looper_1.__next__())
    print(looper_1.__next__())

except StopIteration as e:
    print('Error: Iteration has stopped.')

print('-------------')

# --- using Python iter() function: saving ourself to write double '_'

looper_2 = iter(customers)

try:
    print(next(looper_2))
    print(next(looper_2))
    print(next(looper_2))
    print(next(looper_2))
    print(next(looper_2))

except StopIteration as e:
    print('Error: Iteration has stopped.')

print('-------------')

# ----- using iter and next to replicate a for loop

for person in customers:
    print(person)


print('-------------')


# let's replicate the previous

looper_3 = iter(customers)
while True:
    try:
        print(next(looper_3))
    except StopIteration as e:
        print('Error: Replicate Iteration has stopped.')
        break


print('-------------')
