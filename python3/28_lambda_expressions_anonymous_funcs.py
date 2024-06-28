# !bin/bash
# Daniel OUATTARA
# 28 06 2024


# Write a function to compute 3x + 1


def f(x):
    return 3*x + 1


print(f(2))  # 7


# Write a lambda, single argument

# g = lambda x: x+3 + 1

def g(x): return x+3 + 1

# Write a lambda, multiple argument

# full_name = lambda first_n, last_n: f'{first_n} {last_n}'


def full_name(
    first_n, last_n): return f'{first_n.strip().title()} {last_n.strip().title()}'


print(full_name('John', 'Doe'))


"""
A function with no name: use lambda to write a function 
that order a list of name according to last name value

"""

# initial list
sci_fi_authors = [
    'Isaac Asimov',
    'Arthur C. Clarke',
    'Philip K. Dick',
    'H.G. Wells',
    'Jules Verne',
    'Frank Herbert',
    'Ray Bradbury',
    'Robert A. Heinlein',
    'Ursula K. Le Guin',
    'William Gibson',
    'Orson Scott Card',
    'Neal Stephenson',
    'Douglas Adams',
    'Kurt Vonnegut',
    'Octavia E. Butler',
    'Margaret Atwood',
    'Kim Stanley Robinson',
    'Larry Niven',
    'James S.A. Corey',
    'John Scalzi',
    'Anne McCaffrey',
    'Stanislaw Lem',
    'Greg Bear',
    'Alastair Reynolds',
    'Peter F. Hamilton',
    'C.J. Cherryh',
    'David Brin',
    'China Miéville',
    'Vernor Vinge',
    'Gene Wolfe'
]


# sorted list
sci_fi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(f'sci_fi_authors {sci_fi_authors}')


"""
Function that write functions
quadratic functions

f(x) = ax**2 + bx + c

"""


def build_quadratic_functions(a, b, c):
    """Return quadratic functions: f(x) = ax**2 + bx + c"""
    return lambda x: a * x**2 + b * x + c


f_1 = build_quadratic_functions(2, 3, -5)

print(f_1(0))  # -5
print(f_1(1))  # 0
print(f_1(2))  # 9


print(build_quadratic_functions(3, 0, 1)(2))  # 13
