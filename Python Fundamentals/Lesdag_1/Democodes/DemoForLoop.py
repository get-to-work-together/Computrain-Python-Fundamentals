import random

for i in range(1,100+1):
    print("Leeftijd: ", i)

aantalKeerGooien = int(input("Hoe vaak wil je gooien met de dobbelsteen?"))

for i in range(aantalKeerGooien):
    print("Gooi", (i+1), random.randint(1,6))