import random

getal1 = random.randint(1, 6)
getal2 = random.randint(1, 6)
getal3 = random.randint(1, 6)

print(getal1)
print(getal2)
print(getal3)

som = getal1 + getal2 + getal3

print("som: ", som)

print(getal1>getal2)
print(getal1 == getal3)
print(getal3 <= getal3)


print(getal1>getal2)
print(getal1 == getal3)
print(getal3 <= getal3 or getal1>getal2)
