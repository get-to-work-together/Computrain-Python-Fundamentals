names = []

while True:
    name = input('Enter a name: ')

    if name == '':
        break

    names.append(name)

for i, name in enumerate(sorted(names), start = 1):
    print(i, name)
