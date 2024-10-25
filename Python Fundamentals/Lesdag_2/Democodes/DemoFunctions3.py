import sys
import os
import random


def som(getal1, getal2):
    somGetallen = getal1 + getal2
    return somGetallen

def vermenigvuldig(getal1, getal2):
    return getal1*getal2

def genereerIPAdres():
    lstLijsten = []
    lstGetallen = []

    print(lstLijsten)
    for i in range(0,3):
        for i in range(0,3):
            lstGetallen.append(str(random.randint(0,9)))
            strGetallen = "".join(lstGetallen)
        lstLijsten.append(strGetallen)
    IPadres = ":".join(lstLijsten)
    return IPadres


def main():
    print("Hier start het script.")

    print(som(5,4))
    print(vermenigvuldig(7,2))
    uitkomst = 5 + som(4,2) + vermenigvuldig(7,4)
    print(uitkomst)

    print(genereerIPAdres())

#main()



