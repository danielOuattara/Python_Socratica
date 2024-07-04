# Daniel OUATTARA
# 02 07 2024


"""

CLASSES | OBJECTS

Terms:
------

class
object
instantiate
argument
parameter
attribute of class
method of class
method of instance
"""

# Defining Classes


class Person:
    def __init__(self, f_name, l_name) -> None:
        self.first_name = f_name
        self.last_name = l_name
        self.full_name = f'{f_name} {l_name}'

    def introduction(self):
        print('self = ', self)
        print(f'Hello !\nMy name is {self.full_name}')

    @classmethod
    def help(cls):
        print('class = ', cls)
        print(f'Checking for help ...')


# Create object from class
mike = Person('Mike', 'Wagner')

# Access attribute

print(f'mike fist name = {mike.first_name} ')
print(f'mike last name = {mike.last_name} ')
print(f'mike full name = {mike.full_name} ')
