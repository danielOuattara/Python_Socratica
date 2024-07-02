# Daniel OUATTARA
# 02 07 2024


"""
Decorators
-----------

@function_decorator
def function_name():
    ~~~ function body ~~~


@class_decorator
class Class_Name:
    @method_decorator
    def method_name():
        ~~~ class and method definition ~~~

   
Decorators are a powerful and flexible tool in Python used to 
modify or enhance functions or methods without changing their 
core definition. They allow you to wrap another function, 
thereby altering its behavior.

Decorator Syntax: Decorators are applied using @decorator_name 
syntax above the function definition.

Function Wrapping: Inside the decorator, a wrapper function is 
defined to modify the behavior of the original function.

Returning Functions: Decorators return the wrapper function, 
which replaces the original function.

        
Functions as First-Class Citizens
----------------------------------
In Python, functions are considered first-class citizens, 
which means they can be treated like any other object. 

This allows functions to be passed as arguments to other 
functions, returned as values from other functions, and 
assigned to variables.

"""


#  In Python, function are First Class Citizens that can be nested


import random
import time


def compose(f, g, x):
    return f(g(x))


print(compose(print, len, "Hello Decorator"))


print('---------------------------------------------')


# Functions can be nested

def random_power():
    def f(x):
        return x**2

    def g(x):
        return x**3

    def h(x):
        return x**4

    functions_list = [f, g, h]
    return random.choice(functions_list)

# test random_power()


for i in range(11):
    p = random_power()
    print(p(3))


print('--------------------------------------------- version 1')


def prime_factorization(n):
    start_time = time.time()
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    stop_time = time.time()

    print(f'delta = {stop_time - start_time}')
    return factors


integers = [2**20 + 1, 2**23 + 1, 2**29 + 1, 2**32 + 1]
for n in integers:
    factorization = prime_factorization(n)
    print(f'Prime factorization of {n} = {factorization}\n')


print('--------------------------------------------- version 2')


""" Applying the Decorator manually """


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        print(f'delta = {stop_time - start_time}\n')
        return result

    return wrapper


#  @timer
def prime_factorization_v2(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


# integers = [2**20 + 1, 2**23 + 1, 2**29 + 1, 2**32 + 1]
# for n in integers:
#     factorization = prime_factorization(n)


""" Applying the Decorator manually """
prime_factorization_timer = timer(prime_factorization_v2)

result = prime_factorization_timer(2**29 + 1)
print(f'result = {result}')


print('--------------------------------------------- version 3')


""" Using Decorator syntax """


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        print(f'delta = {stop_time - start_time}\n')
        return result

    return wrapper


@timer
def prime_factorization_v2(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


integers = [2**20 + 1, 2**23 + 1, 2**29 + 1, 2**32 + 1]
for n in integers:
    factorization = prime_factorization_v2(n)
