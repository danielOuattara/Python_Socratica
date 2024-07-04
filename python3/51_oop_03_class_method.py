# Daniel OUATTARA
# 02 07 2024


"""
Class method

"""

# Defining Class


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

print('------------------')
"""TypeError: Person.introduction() missing 1 required positional argument: 'self'"""
# Person.introduction()

"""Ok, if you pass the instance 'mike' as argument"""
Person.introduction(mike)

print('------------------')
Person.help()  # OK

print('------------------')
mike.help()  # OK

print('------------------')
print(isinstance(mike, Person))  # True
