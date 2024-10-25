import random

dice = []
for i in range(1, 6):
    if i > 2:
        dice.append(random.randint(1, 6))

# dice = [random.randint(1, 6) for i in range(1, 6) if i > 2]

total = sum(dice)

print(dice)
print(total)
