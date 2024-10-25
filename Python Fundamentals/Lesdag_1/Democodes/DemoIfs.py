invoer = input("Voer wat in: ").upper()

be1 = invoer[0] == 'A'
be2 = invoer[0] == 'B'
be3 = invoer[0] == 'C'

if be1 or be2:
    if invoer[1] != 'A':
        print("De eerste letter is een A of B, maar de 2e letter is geen A.")
    else:
        print("De eerste letter is een A of B, maar de 2e letter is wel een A.")
elif be3:
    print("De eerste letter is C.")
elif invoer[-1] == "?":
    print("De laatste letter is een vraagteken.")
else:
    print("De eerste letter is geen A, B en C.")

print("Dit is het einde.")

getal = 1000 if invoer.lower()[0] == 'j' else 100

print("getal:", getal)