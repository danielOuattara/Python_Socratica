# !bin/bash
# Daniel OUATTARA
# 28 06 2024


""" Sorting """


earth_metals_list = [
    'Beryllium',
    'Magnesium',
    'Calcium',
    'Strontium',
    'Barium',
    'Radium'
]


print(f'earth_metals_list {earth_metals_list}')


#
earth_metals_list.sort()
print(f'earth_metals_list {earth_metals_list}')

#
earth_metals_list.sort(reverse=True)
print(f'earth_metals_list {earth_metals_list}')


# print(help())


planets = [
    # (name, radius(km), density(g/cm3), distance from SUn(AUs))
    ('Mercury', 2439.7, 5.427, 0.39),
    ('Venus', 6051.8, 5.243, 0.72),
    ('Earth', 6371.0, 5.513, 1.0),
    ('Mars', 3389.5, 3.933, 1.52),
    ('Jupiter', 69911, 1.326, 5.20),
    ('Saturn', 58232, 0.687, 9.58),
    ('Uranus', 25362, 1.270, 19.22),
    ('Neptune', 24622, 1.638, 30.05)
]


#  ---> Sort the planets by radius decreasing values
# planet_size = lambda planet: planet[1]


def planet_size(planet): return planet[1]


planets.sort(key=planet_size, reverse=True)

print(f'planets by radius decreasing values = {planets}')

print('-------------------------------------------')

# ---> Sort the planets by radius decreasing values


# planet_density = lambda planet: planet[2]
def planet_density(planet): return planet[2]


planets.sort(key=planet_density, reverse=True)

print(f'planets by density decreasing values = {planets}')

print('-------------------------------------------')


# How to create a sorted copy ?
# How to sort tuple ?
# use : sorted()

earth_metals_list = [
    'Beryllium',
    'Magnesium',
    'Calcium',
    'Strontium',
    'Barium',
    'Radium'
]


#
earth_metals_list_sorted = sorted(earth_metals_list)
print(f'earth_metals_list_sorted = {earth_metals_list_sorted}')

#
earth_metals_list_sorted_reverse = sorted(earth_metals_list, reverse=True)
print(f'earth_metals_list_reverse = {earth_metals_list_sorted_reverse}')


data = (7, 2, 4, 8, 10, 13, 56, 11)
print(sorted(data))


#
print(sorted("Alphabetical"))
