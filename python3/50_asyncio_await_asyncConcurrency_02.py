# Daniel OUATTARA
# 02 07 2024

import time
import asyncio


def brewCoffee():
    print("Start brew some coffee")
    time.sleep(3)
    print("End brew some coffee")
    return "Coffey Ready"


def toastBagel():
    print("Start toast some bagel")
    time.sleep(2)
    print("End toast some bagel")
    return "Bagel Toasted"


def main():
    start_time = time.time()

    result_coffee = brewCoffee()
    result_bagel = toastBagel()
    end_time = time.time()

    delta = end_time - start_time

    print(f'Result of brewCoffee: {result_coffee}')
    print(f'Result of toastBagel: {result_bagel}')
    print(f'Total execution time: {delta}\n')


""" 
Problem: time waisted 

Details: there is no reason to wait for the coffee 
         to finish before you start toasting


Solution: Modify the code so it runs concurrently 
          using coroutines
          

Practically: turn each functions in coroutines, as show bellow

"""


async def brewCoffee_2():
    print("Start brew some coffee")
    await asyncio.sleep(3)
    print("End brew some coffee")
    return "Coffey Ready"


async def toastBagel_2():
    print("Start toast some bagel")
    await asyncio.sleep(2)
    print("End toast some bagel")
    return "Bagel Toasted"


# ------------------------------------------------


async def main_2():
    start_time = time.time()

    """ (1): Running Coroutines Concurrently """
    # batch = asyncio.gather(brewCoffee_2(), toastBagel_2())
    # result_coffee, result_bagel = await batch

    """ (2): Running Coroutines Concurrently """
    # result_coffee, result_bagel = await asyncio.gather(brewCoffee_2(), toastBagel_2())

    """ (3): Using asyncio.create_task() functions """
    coffee_task = asyncio.create_task(brewCoffee_2())
    toast_task = asyncio.create_task(toastBagel_2())

    result_coffee = await coffee_task
    result_bagel = await toast_task

    end_time = time.time()
    delta = end_time - start_time

    print(f'Result of brewCoffee_2: {result_coffee}')
    print(f'Result of toastBagel_2: {result_bagel}')
    print(f'Total execution time on async: {delta}\n')


if __name__ == '__main__':
    main()
    asyncio.run(main_2())
