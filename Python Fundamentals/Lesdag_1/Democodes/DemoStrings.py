naam = "Martijn"
jaar = 1981
print("Martijn is geboren in " + str(jaar))
print("Martijn is geboren in ", jaar)

film = 'De film "Spiderman"'
film2 = "De film \"Spiderman\""
plaats = '\'s-Hertogenbosch'
plaats2 = "'s-Gravenhage"

naamfilm = naam + " gaat naar " + film +  " in " + plaats + " en " + plaats2 +"."
print(naamfilm)

naamfilm.format()

getal = 100
geborenFomat = "%s is geboren in %d %d." % (naam, jaar, getal)

print(geborenFomat)
print(type(geborenFomat))

geborenFformat = f'{naam} is geboren in {jaar}'
print(geborenFformat)

geborenFormatLiefst = "{} is geboren in {}".format(naam, jaar)
print(geborenFormatLiefst)

print(geborenFormatLiefst.split(" "))
