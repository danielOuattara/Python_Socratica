# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


""""
CSV: comma separated values.

A popular format for storing data,

CSV is simple and convenient

Python has a CSV module to handle it

To be useful, we need to store the data

1- without CSV module
2- with CSV module

"""

path = "./20_google_stock_data.csv"

# file = open(path)

# for line in file:
#     print(line.strip())

# lines = [line for line in open(path)]

# print(lines)

# print(lines[0])
# print(lines[1])

#  handle data
# ==============

# print(lines[0].strip())

# print(lines[0].strip().split(','))

# ----------------------------------------------

dataset = [line.strip().split(',') for line in open(path)]

print(dataset[0])
print(dataset[1])
