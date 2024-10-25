magicNumber = 11

for i in range(1, 21):
    print(i, end=" ")
    if i == magicNumber:
        break
    print("|", end="")

print()

for i in range(1, 21):
    print(i, end=" ")
    if i == magicNumber:
        continue
    print("|", end="")

