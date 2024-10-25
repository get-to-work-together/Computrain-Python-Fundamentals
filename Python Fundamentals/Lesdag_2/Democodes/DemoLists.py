lstNamen = ["Martijn", "Tonito"]

print(lstNamen)
#lstNamen.append(True)
lstNamen.append("Edwin")

print(lstNamen)


#lstNamen.append(100)

print(lstNamen)

print(type(lstNamen))

lstNamen.insert(2, "Hans")
print(lstNamen)

lstNamen.extend(["Wijnald", "Harry"])

print(lstNamen)


laatste = lstNamen.pop()

print(lstNamen)
print(laatste)

lstNamen.sort()
print(lstNamen)

lstGetallen = list(range(1,1000,2))

print(lstGetallen)