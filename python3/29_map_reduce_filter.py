# !bin/bash
# Daniel OUATTARA
# 28 06 2024


from functools import reduce
import statistics
import math


"""=== MAP ==="""

""" Example on Area calculation
-------------------------------- """


def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * r**2


radii = [2, 5, 7.1, 0.3, 10]

#  Method 1 : direct method

areas_list_1 = []
for radius in radii:
    a_calculated = area(radius)
    areas_list_1.append(a_calculated)

print(f'areas_list_1 = {areas_list_1}')
print('-------')

# Method 2 : use map function

areas_list_2 = map(lambda r: math.pi * r**2, radii)
print(f'areas_list_2 = {list(areas_list_2)}')
print('-------')

"""
Example on convert the temperature value from °C to °F
------------------------------------------------------- """

city_temperatures_celsius = [
    ("New York", 12.5),
    ("London", 11.1),
    ("Tokyo", 15.6),
    ("Sydney", 18.0),
    ("Paris", 12.3),
    ("Moscow", 5.8),
    ("Cairo", 22.8),
    ("Beijing", 13.3),
    ("Los Angeles", 18.5),
    ("Mumbai", 27.2),
    ("Rio de Janeiro", 23.2),
    ("Cape Town", 17.0),
    ("Berlin", 10.0),
    ("Toronto", 8.5),
    ("Buenos Aires", 17.3),
    ("Mexico City", 15.9),
    ("Jakarta", 27.6),
    ("Istanbul", 14.1),
    ("Dubai", 28.2),
    ("Seoul", 12.3),
    ("Bangkok", 28.1),
    ("Singapore", 27.0),
    ("Madrid", 14.5),
    ("Rome", 15.7),
    ("Lagos", 27.0)
]

print(f'city_temperatures_celsius =  {city_temperatures_celsius}')

print('-------')


# celsius_to_fahrenheit = lambda city: (city[0], round(city[1] * 9/5 + 32, 2))


def celsius_to_fahrenheit(city): return (city[0], round(city[1] * 9/5 + 32, 2))


city_temperatures_fahrenheit = list(
    map(celsius_to_fahrenheit, city_temperatures_celsius))

print(f'city_temperatures_fahrenheit =  {city_temperatures_fahrenheit}')

print('-----------------------------------------------------')


"""=== FILTER ==="""

""" Example: Find all data above the average
--------------------------------------------- """

# import statistics


temperatures_celsius = [
    12.5,
    11.1,
    15.6,
    18.0,
    12.3,
    5.8,
    22.8,
    13.3,
    18.5,
    27.2,
    23.2,
    17.0,
    10.0,
    8.5,
    17.3,
    15.9,
    27.6,
    14.1,
    28.2,
    12.3,
    28.1,
    27.0,
    14.5,
    15.7,
    27.0
]

average = statistics.mean(temperatures_celsius)
print(f'average = {average}')  # 17.74

# Use the filter method to keep value above the average

above_mean_temperature = filter(
    lambda value: value > average, temperatures_celsius)

print(f'list(above_mean_temperature) = {list(above_mean_temperature)}')


""" Example: Removing missing data
---------------------------------- """

south_american_countries = [
    "Argentina",
    "",
    "Bolivia",
    "Brazil",
    "",
    "Chile",
    "Colombia",
    "Ecuador",
    "",
    "Guyana",
    "Paraguay",
    "Peru",
    "Suriname",
    "",
    "Uruguay",
    "Venezuela",
    ""
]

filtered_countries = filter(None, south_american_countries)
print(f'filtered_countries={list(filtered_countries)}')


"""=== REDUCE ==="""

""" Example: inner Multiply all temp value above
------------------------------------------ """

# multiplier = lambda x,y: x*y


def multiplier(x, y): return x*y


result = reduce(multiplier, temperatures_celsius)
print(f'result {result}')


# OR

result_2 = 1

for value in temperatures_celsius:
    result_2 *= value

print(f'result_2 {result_2}')
