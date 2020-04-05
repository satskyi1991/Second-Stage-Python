list1 = [1, 2, 3, 4, 5]

iterator = iter(list1)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
iterator = iter(list1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

import random


class RandomGeneratorIterator:

    def __init__(self, random_generator_instance):
        self._instance = random_generator_instance
        self._instance._start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._instance._start < self._instance._quantity:
            self._instance._start += 1
            return random.randint(0, 100)
        raise StopIteration()


class RandomGenerator:

    def __init__(self, quantity_of_random_nums):
        self._quantity = quantity_of_random_nums
        self._start = 0

    def __iter__(self):
        return RandomGeneratorIterator(self)



randge = RandomGenerator(4)
for i in randge:
    print(i)

for i in randge:
    for j in randge:
        print(j)
