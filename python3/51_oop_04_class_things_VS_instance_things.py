# Daniel OUATTARA
# 02 07 2024


"""
Class things VS Object/instance things

- class attributes : belong to Class, and available to objects

- instance attributes: belong to object , not available to Class

- Class methods: require the decorator '@classmethod', 
                 and are called by the Class or instance of the Class

- instance methods: have access to ALL Class things and instance things 
"""

# Defining Class


class Person:
    counter = 0  # class attributes

    def __init__(self, name) -> None:
        self.full_name = name  # instance attribute
        Person.counter += 1  #  increment the class attribute

    def introduction(self):
        print('self = ', self)
        print(f'Hello !\nMy name is {self.full_name}')

    @classmethod
    def population(cls):
        print('class = ', cls)
        print(f'The current population is {cls.counter} ...')


# Create object from class
mike = Person('Mike Wagner')
mike.introduction()
mike.population()

print('-------------------------------------------')
john = Person('John Doe')
mike.introduction()
mike.population()
