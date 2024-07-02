import time

t0 = time.time()


def _test_prime(n):
    for i in range(8, n):
        if i == 2:
            print(i, "is prime")
        if i == 3:
            print(i, "is prime")
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i, "is prime")
        else:
            print(i, "not a prime")


t1 = time.time()
nombre = int(input(print("enter un grand nombre:")))
_test_prime(nombre)

print("deltaTime = ", t1 - t0)
