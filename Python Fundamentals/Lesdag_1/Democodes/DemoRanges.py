langeZin = "Dit is een lange zin."

for nummer in range(20):
    print(nummer, end=" ")

print()

for nummer in range(10, 20):
    print(nummer, end=" ")

print()

for nummer in range(0, len(langeZin), 2):
    print(langeZin[nummer], end=" ")

print()

for nummer in range(100, 1, -5):
    print(nummer, end=" ")