# Daniel OUATTARA
# 01 07 2024

""" 
Special methods and attributes

__method_name__

used to:
- empowered your classes with custom behavior for standard syntax
- override operators
- define iterations
- access the inner workings of classes
- etc...



Special methods and attributes in Python serve several important 
purposes, enhancing the functionality and flexibility of classes 
and objects. 

Here's an exhaustive look at their purposes:


1- Customizing Behavior: Special methods allow classes to define 
how instances behave when used in operations like addition (__add__), 
comparison (__lt__, __eq__, etc.), or conversion to strings 
(__str__, __repr__). This customization makes instances of a class 
behave more intuitively and can tailor their behavior to specific 
use cases.


2- Operator Overloading: Python allows operators such as +, -, *, 
etc., to be overloaded using special methods. This means that the 
behavior of these operators can be customized for objects of 
user-defined classes, enabling more natural syntax and operations.


3- Controlling Attribute Access: Special methods like __getattr__, 
__setattr__, and __delattr__ provide control over how attributes 
are accessed, set, or deleted on instances. This enables validation, 
logging, or computation on attribute access.


4- Iteration and Collection: Methods like __iter__, __next__ 
(__iter__, __getitem__ in Python 2.x), and __contains__ allow instances 
of a class to be iterable or behave like collections (e.g., lists, 
dictionaries). This is essential for creating custom iterable objects 
or defining custom containers.


5- String Representation: Methods like __str__, __repr__, and __format__ 
define how instances are converted to strings. This affects how instances 
are displayed when printed, interacted with in debugging, or formatted as strings.


6- Callable Objects: Instances can be made callable by defining the __call__ 
method. This allows objects to be invoked as functions, providing a way to 
encapsulate behavior with internal state.


7- Context Management: Methods like __enter__, __exit__ enable objects to 
support the context management protocol (with statement). This is useful 
for resource management (e.g., file handling, database connections) where 
setup and cleanup actions are needed.


8- Descriptor Protocol: Special methods like __get__, __set__, and __delete__ 
allow classes to define how attributes are accessed through descriptors. 
This is advanced Python functionality used to implement properties and manage 
attribute access behavior.


9- Customizing Container Behavior: Methods like __len__, __getitem__, __setitem__, 
and __delitem__ enable classes to behave like containers (e.g., lists, dictionaries). 
This is crucial for defining custom data structures or enhancing existing ones.


10- Metaprogramming: Special methods facilitate metaprogramming by allowing 
classes to define custom behavior for operations like class instantiation 
(__new__, __init__), attribute access (__getattribute__, __getattr__), and 
instance creation (__call__, __new__).


In summary, special methods and attributes in Python are fundamental 
for customizing how instances of classes behave in terms of operators, 
attribute access, iteration, string representation, callable behavior, 
context management, container-like behavior, and metaprogramming. 

They empower developers to create more expressive, flexible, and tailored 
classes and objects within Python's object-oriented framework.


"""


from typing import Any


class Snowflake:
    pass


flake = Snowflake()

# for item in dir(flake):
#     print(item)

"""
__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
__weakref__"""


print('---------------------------------------')


class Martian:
    pass


# __dict__: to store class's instance attribute

john = Martian()
print(john.__dict__)  # {}

john.first_name = 'John'
john.last_name = 'Doe'
print(john.__dict__)  # {'first_name': 'John', 'last_name': 'Doe'}


print('---------------------------------------')


class Martian_2:
    """Someone who lives on Mars"""

    def __init__(self, f_name, l_name) -> None:
        self.first_name = f_name
        self.last_name = l_name


print(Martian_2.__doc__)  # {}

jane = Martian_2(f_name='Jane', l_name='Jones')
jane.born_date = '4983-12-15'
print(jane.__dict__)


print('---------------------------------------')


class Boxer:
    """Someone who punches like a volcano"""

    def __init__(self, f_name, l_name) -> None:
        self.first_name = f_name
        self.last_name = l_name

    def __setattr__(self, name: str, value: Any) -> None:
        print(f'>>> You set {name} = {value}')
        self.__dict__[name] = value


mike = Boxer(f_name='Mike', l_name='Tyson')
print(mike.__dict__)


print('---------------------------------------')


class Scottish:
    """ Someone who lives in Scotland """

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __setattr__(self, name, value):
        print(f'>>> You set {name} = {value}')
        self.__dict__[name] = value

    def __getattr__(self, name):
        print(f'>>> Get the {name} attribute')

        if name == 'full_name':
            return f'{self.first_name} {self.last_name}'
        else:
            raise AttributeError(f'No attribute name {name}')


bow = Scottish(f_name='Bow', l_name='Sparrow')
print(f'First name = {bow.first_name}')
print(f'Last name = {bow.last_name}')
print(bow.full_name)

# print(bow.date_of_birth)  # AttributeError

print(bow.__dict__)

print('---------------------------------------')


class Coder:
    """ Someone who talks to computer """

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __setattr__(self, name, value):
        self.__dict__[name] = value


steeve = Coder(f_name='Steeve', l_name='Jobs')
print(steeve)
print(steeve.__str__())
print(id(steeve))


print('---------------------------------------')


class Player:
    """ Someone who plays games """

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


joker = Player(f_name='Joker', l_name='Monopoly')
print(joker)
print(id(joker))


print('---------------------------------------')


class People:
    """ Humans who walks in street ;) """

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __lt__(self, other):
        print(f'--> Comparing {self} with {other}')
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)


p1 = People('Cyril', 'Collin')
p2 = People('Len', 'Klein')
p3 = People('Mathias', 'Stein')
p4 = People('Mike', 'Tyson')
p5 = People('Bob', 'Harley')
p6 = People('Owen', 'Meek')
p7 = People('Andy', 'Taylor')
p8 = People('Albert', 'Stone')
p9 = People('Marin', 'Milk')


people_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
people_list.sort()
for p in people_list:
    print(p)
