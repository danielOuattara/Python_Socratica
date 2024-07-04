# Daniel OUATTARA
# 02 07 2024


"""
Instance method

attributes: design characteristic of object 
method: different capabilities of object  
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


print('------------------')
# use mike method
mike.introduction()
