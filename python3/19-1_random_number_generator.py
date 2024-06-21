# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


"""
WARNING: The pseudo-random generators of this module should not
         be used for security purposes.

         Use os.urandom() or SystemRandom if you require a 
         cryptographically secure pseudo-random number generator

"""

import random
from os import urandom


# for item in dir(random):
#     print(item)


#  print(help(random.random))

# generate and display 10 random numbers from [ 0, 1)

for n in range(1, 11):
    print(random.random())

print('-' * 40)

# generate and display 10 random numbers from [ 3, 7)

# (1)
for n in range(1, 11):
    value = random.random() * 4 + 3
    print(value)

print('-' * 20)

# (2)


for n in range(1, 11):
    print(random.uniform(3, 7))


"""
NOTE: random() & uniform() both follow the uniform probability distribution
"""
print('-' * 40)

# generate and display 20 random numbers from the normal distribution

"""
normalvariate(mu, sigma)

"""

for n in range(21):
    print(random.normalvariate(0, 1))

print('-' * 20)

for n in range(21):
    print(random.normalvariate(0, 4))

print('-' * 20)

for n in range(21):
    print(random.normalvariate(4, 1))

print('-' * 40)


# generate and display 10 random numbers
# from the discrete probability distribution

for n in range(11):
    print(random.randint(1, 6))

print('-' * 40)


# display 10 random element from a list
outcomes = ['rock', 'paper', 'scissor']

for n in range(11):
    print(random.choice(outcomes))
