getal = 10/10

print(getal)

getal2 = 10/0.0001

print(getal2)

print(getal3)

while True:
    name = input('Geef een naam: ')
    print(name)
    if name.lower() == 'exit':
        raise Exception("Exit de loop")
