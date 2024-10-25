setGetallen = {1,2,3}
print(type(setGetallen))

dctWoorden = {"a":1, "b":2, "c":3}
print(type(dctWoorden))

dctStudenten = {}
print(dctStudenten)
print(type(dctStudenten))
dctStudenten["Jarno"] = 34
dctStudenten["Marc"] = 30
dctStudenten["Jordy"] = 30
dctStudenten["Niek"] = 30
dctStudenten["Omar"] = 50

print(dctStudenten)

print("De leeftijd van Niek is:", dctStudenten["Niek"])

print(dctStudenten)

dctStudenten[6] = 100

print(dctStudenten)

dctStudenten[7.4] = 1000

print(dctStudenten)

lstGetallen = [1,2,3]
tplGetallen = tuple(lstGetallen)

dctStudenten[tplGetallen] = "Springen en dansen"

print(dctStudenten)

dctStudenten['Jarno'] = dctStudenten['Jarno'] * 2

print(dctStudenten)

print(dctStudenten.keys())
print(type(dctStudenten.keys()))

#lstKeysDctStudenten = sorted(list(dctStudenten.keys()))

dctStudenten["Marc"] = ["Marc", "Hoofdstraat 10", "Utrech"]

for sleutel in dctStudenten.keys():
    print(sleutel, ":", dctStudenten[sleutel], type(dctStudenten[sleutel]))

dctStudenten["Woorden"] = dctWoorden

print(dctStudenten["Woorden"]["a"])

print(dctStudenten.keys())
print(type(dctStudenten.keys()))
lstKeysVanDctStudenten = sorted(list(dctStudenten.keys()))
print(lstKeysVanDctStudenten)

print(dctStudenten.values())
print(type(dctStudenten.values()))

for k in lstKeysVanDctStudenten:
    print(k, dctStudenten[k])