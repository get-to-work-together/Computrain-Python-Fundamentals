woord = input("Geef een woord: ")

# Elke letter wordt getoond op het beeldscherm.
for letter in woord:
    print(letter, end=" ")

print()

for li in range(len(woord)):
    #print(li, end=" ")
    print(woord[li], end=" ")

print()

for li in range(1, len(woord), 2):
    #print(li, end=" ")
    print(woord[li], end=" ")