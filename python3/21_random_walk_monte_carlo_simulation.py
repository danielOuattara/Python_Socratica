# !bin/bash
# Daniel OUATTARA
# 24 06 2024


"""
What is the longest random walk you can take, 
so that on average you will end up 4 blocks or 
fewer from home ?

"""

# The plan : write the random walk function 2 versions ( simple & short)

import random


def random_walk_1(n):
    """ Return coordinates after 'n' block random walk"""

    x = y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])

        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x += 1

    return (x, y)


for i in range(25):
    walk = random_walk_1(10)
    print(f'{walk} Distance from home = {abs(walk[0]) + abs(walk[1])}')


# ----------------------------------------------
print('-' * 40)


def random_walk_2(n):
    """ Return coordinates after 'n' block random walk"""

    x = y = 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


for i in range(25):
    walk = random_walk_1(10)
    print(f'{walk} Distance from home = {abs(walk[0]) + abs(walk[1])}')


# --------------------------------------------- Monte Carlo
print('-' * 40)

number_of_walks = 20_000

for walk_length in range(1, 31):
    no_transport = 0  # number of walks 4 or fewer blocks to home

    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)

        if distance < 5:
            no_transport += 1

    no_transport_percentage = float(no_transport / number_of_walks)
    print(
        f'Walk size =  {walk_length}, no_transport {no_transport_percentage:.2%}')
