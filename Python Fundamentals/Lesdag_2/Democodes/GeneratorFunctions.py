import random

def random_order1(numbers):
    random.shuffle(numbers)
    for number in numbers:
        yield number

def random_order2(numbers):
    random.shuffle(numbers)
    yield from numbers

x = random_order1([1,3,3,4,3,5,3])

print(x)



