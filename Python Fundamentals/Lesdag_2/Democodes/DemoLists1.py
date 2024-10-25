getal1 = 10
getal2 = 20
getal3 = 30
getal4 = 40
getal5 = 50

lstGetallen = [10, 20, 30, 40, 50]

getalMidden = lstGetallen[2]

lstGetallenTm1000 = list(range(1000,10-1, -10))

print(lstGetallen)
print(lstGetallenTm1000)

lstZomaarWaarden = [1, 5.0, "Hallo", True, -8, complex(2)]

print(lstZomaarWaarden[1])

print(type(lstZomaarWaarden[1]))

for waarde in lstZomaarWaarden:
    print(waarde, "is van datatype", type(waarde))

