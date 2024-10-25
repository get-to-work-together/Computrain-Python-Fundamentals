lstNames = []

# Names are given here.
while True:
    name = input("Give a new name: ")
    name = name.strip()
    if name == "":
        break

    lstNames.append(name)

# Names are sorted and shown.
lstNames.sort()

lstNames2 = sorted(lstNames)

for name in lstNames:
    print(name)

print(lstNames)
