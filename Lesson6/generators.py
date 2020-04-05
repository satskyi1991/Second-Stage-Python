import random


#generator function
def random_generator(qnt_of_random_numbers):
    start = 0

    while start < qnt_of_random_numbers:
        start += 1
        yield random.randint(0, 100)
        print('AFter yield')
        yield random.randint(0, 100)


gen = random_generator(3)


#genexpr
randoms = (random.randint(0, 100) for i in range(10))

type(randoms)
for i in randoms:
    print(i)
