import random

def random_order1(numbers):
    random.shuffle(numbers)
    for number in numbers:
        yield number

def random_order2(numbers):
    random.shuffle(numbers)
    yield from numbers

lstGetallen = [3,5,3,6,3,6,3,6,7,2,6]

lst1 = random_order1(lstGetallen)
lst2 = random_order2(lstGetallen)

print("lst1:\n")
for li in lst1:
    #g = input()
    print(li)

print("\nlst2:\n")
for li in lst2:
    print(li)