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


class Portfolio:
    def __init__(self):
        self.holdings = {}  # where key = ticker, value = number of shares

    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())


p = Portfolio()

p.buy('ALPHA', 15)
p.buy('BETA', 23)
p.buy('GAMMA', 9)
p.buy('GAMMA', 20)


for (ticker, shares) in p:
    print(ticker, shares)
