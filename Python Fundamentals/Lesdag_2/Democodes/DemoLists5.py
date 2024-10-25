lijst1 = []

lijst1.append("Jordy")
lijst1.append(50)
lijst1.append(8.0)
lijst1.append(True)
lijst1.append([1,23])


print(lijst1)

print(type("Jordy"))
print(type(50))
print(type(8.0))
print(type(True))

print(type(lijst1))

lijst1.extend(['Martijn', 50, 78, 50, 8.0])

print(lijst1)

lijst1.remove(50)
print(lijst1)

naam = "Omar"

lijst1.append(naam)

print(lijst1)

#lijst1.sort()
lijst1.reverse()

print(lijst1)
del lijst1

print(lijst1)