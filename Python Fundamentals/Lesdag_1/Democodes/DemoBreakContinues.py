magischGetal = 10

for getal in range(1, 31):
    if getal % magischGetal == 0:
        print("X")
        break
    print(getal, end=" ")

print("De loop is gebroken.")

for getal in range(1, 31):
    if getal % magischGetal == 0:
        print("X")
        continue
    print(getal, end=" ")

print("De iteratie is gebroken.")

