zin = input("Geef een zin op: ")

sp = input("Op welke letter wil je de zin splitten? ")

lstWoordjes = zin.split(sp)

print(lstWoordjes)

jn = input("Op welke letter wil je de zin joinen? ")

nieuweZin = jn.join(lstWoordjes)

print(nieuweZin)
