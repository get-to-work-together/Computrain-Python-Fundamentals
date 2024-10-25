naam1 = "Martijn 2"
naam2 = "Brian"
naam3 = "Tessa"
naam4 = naam1
naam5 = "Brian 2"

print("De adressen van de volgende namen zijn als volgt:")

print(naam1, "heeft adres: ", hex(id(naam1)))
print(naam2, "heeft adres: ", hex(id(naam2)))
print(naam3, "heeft adres: ", hex(id(naam3)))

print(naam4, "heeft adres: ", hex(id(naam4)))
print(naam5, "heeft adres: ", hex(id(naam5)))

