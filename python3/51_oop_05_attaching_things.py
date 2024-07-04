# Daniel OUATTARA
# 04 07 2024


import types

"""
Attaching things.

- in the previous definition we included the attributes and methods
  in the class definition: this is typical of languages like C and Java 

- in Python, attributes and methods are also defined in class definition
  AND they can also attached later

- 'monkey patching' = dynamically attaching an attribute or method to 
                      a class or object
  
"""


class Person:  # Defining Class
    counter = 0  # class attributes

    def __init__(self, name) -> None:
        self.full_name = name  # instance attribute
        Person.counter += 1  # increment the class attribute

    def introduction(self):
        print('self = ', self)
        print(f'Hello !\nMy name is {self.full_name}')

    @classmethod
    def population(cls):
        print('class = ', cls)
        print(f'The current population is {cls.counter} ...')


# Create object from class
mike = Person('Mike Wagner')
john = Person('John Doe')


# Attach a coin balance attribute to mike only
mike.coin = 1_618_033

print(dir(mike))
print('--------------------------------------')
print(dir(john))

# Attach a version attribute to Class itself
Person.version = 1.0

print('\n\n\n')
print(dir(mike))
print('--------------------------------------')
print(dir(john))
print('--------------------------------------')
print(dir(Person))


# define a function to be attached to the instance
def add_coins(self, amount):
    self.coin += amount
    print(
        f'Add {amount} coins\nNew coins balance for {self.full_name}: {self.coin}')


# attach the add_coins() function to the instance 'Mike' only
mike.add_coins = types.MethodType(add_coins, mike)


# Test the newly attached method
mike.add_coins(500)

print('\n\n\n')
print(dir(mike))
print('--------------------------------------')
print(dir(john))
print('--------------------------------------')
print(dir(Person))


# define a function to be attached to the class
def class_method(cls):
    print(f'This is a method attached to the {cls.__name__} class.')


# Attach the function to the class 'Person'
Person.class_method = classmethod(class_method)


# Test the newly attached class method
Person.class_method()
mike.class_method()  # This will also work because 'class_method' is now part of the class


# ---------------------------------------------------------------------


"""
Key Points
----------
- Deleting an Instance Attribute: Use 'del instance.attribute'.

- Deleting a Class Attribute: Use 'del Class.attribute'.

- Deleting an Instance Method: Use 'del instance.method'.

- Deleting a Class Method: Use 'del Class.method'.

"""

# Define the class


class Human:
    species = 'Homo sapiens'  # Class attribute

    def __init__(self, name):
        self.full_name = name
        self.age = 30

    def introduction(self):
        print(f'Hello, my name is {self.full_name}.')

    @classmethod
    def class_method(cls):
        print(f'This is a method attached to the {cls.__name__} class.')


# Create an instance of the class
mike = Human('Mike Wagner')

# Delete an instance attribute
del mike.age

# Delete a class attribute
del Human.species

# Delete an instance method by removing it from the class
del Human.introduction

# Delete a class method
del Human.class_method

# Attempt to access or call the deleted attributes and methods
try:
    print(mike.age)
except AttributeError as e:
    print(e)  # Outputs: 'Human' object has no attribute 'age'

try:
    print(Human.species)
except AttributeError as e:
    print(e)  # Outputs: type object 'Human' has no attribute 'species'

try:
    mike.introduction()
except AttributeError as e:
    print(e)  # Outputs: 'Human' object has no attribute 'introduction'

try:
    Human.class_method()
except AttributeError as e:
    print(e)  # Outputs: type object 'Human' has no attribute 'class_method'
