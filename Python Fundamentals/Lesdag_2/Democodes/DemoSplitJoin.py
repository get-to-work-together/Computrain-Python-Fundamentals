zin = "Het is vandaag lekker weer."

partsZin = zin.lower().split(" ")

print(partsZin)

partsZin.sort()

print(partsZin)

nieuweZin = "_".join(partsZin)

print(nieuweZin)