
zin = "Hallo, het is heet."

for i in range(0, len(zin)):
    if i % 2 == 0:
        print(zin[i], end = " ")

print()

for i in range(0, len(zin), 2):
    print(zin[i], end = " ")

print()


