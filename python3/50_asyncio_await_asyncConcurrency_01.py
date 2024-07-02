# Daniel OUATTARA
# 02 07 2024


"""

https://docs.python.org/3.11/library/asyncio.html#module-asyncio

asyncio await async concurrency


code = synchronous OR asynchronous

asynchronous code save time
                  ----------  

subroutine: a block that can be called when needed
----------

main thread-->|                       |--> then back to main thread
              |                       |
              °--> then subroutine -->°
                    call & execution

NOTE: Subroutine cannot be paused and resumed,
      they run until their are done 

coroutine
---------

NOTE: They can be paused and resumed, because 
      they maintain their state between pauses

coroutine is perfect for applications: 
- i/o operations
- databases queries
- http requests

Many coroutines can run in concurrency* & parallelism*

- concurrency: start & stop times of multiples coroutines can overlap
- parallelism: different threads can execute at the same time


Python concurrency:

1- async keyword

2- await keyword

3- asyncio keyword

"""
