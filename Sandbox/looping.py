


counter = 1
while counter <= 10:
    print(counter)
    counter += 1




counter = 1
while True:
    print(counter)
    counter += 1
    if counter > 10:
        break


eol = False
counter = 1
while not eol:
    print(counter)
    counter += 1
    if counter > 10:
        eol = True


for getal in [1,2,3,4,5,6,7,8,9,10]:
    print(getal)

for getal in [3,7,2,8,4,5]:
    print(getal * 100)
    if getal == 8:
        break

for getal in range(1, 11):
    print(getal)

for getal in list(range(1, 11)):
    print(getal)


for woord in 'dit zijn een aantal woorden'.split():
    print(woord)




