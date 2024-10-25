lstNames = []

name = input("Give a new name: ")
# Names are given here.
while name != "":
    lstNames.append(name)
    name = input("Give a new name: ")

# Names are sorted and shown.
lstNames.sort()

for name in lstNames:
    print(name)

print(lstNames)