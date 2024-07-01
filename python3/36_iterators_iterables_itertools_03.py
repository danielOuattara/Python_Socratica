# Daniel OUATTARA
# 01 07 2024


"""
Iterators Iterables Itertools

In Python if you can loop over something, then that something
is called an iterable

- a sequence = iterable + ordered
- common sequences: lists, tuples, strings, bytes

What makes an object iterable ???

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
    Return the ext item from the container
    If there are no further items to iterate over, 
    raise the StopIteration exception
"""

import itertools


# for item in dir(itertools):
#     print(item)


"""
__doc__
__loader__
__name__
__package__
__spec__
_grouper
_tee
_tee_dataobject
accumulate
chain
combinations
combinations_with_replacement
compress
count
cycle
dropwhile
filterfalse
groupby
islice
pairwise
permutations
product
repeat
starmap
takewhile
tee
zip_longest
"""


ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

ranks = [str(rank) for rank in ranks]
print(ranks)

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [card for card in itertools.product(ranks, suits)]

for (index, card) in enumerate(deck):
    print(1 + index, card)

hands = [hand for hand in itertools.combinations(deck, 5)]
print(f'The number of 5-card poker hands is {len(hands)}')
