woorden = "Leuk woordje\tLeuke woordje 2\nLeuk woordje 3"

print(woorden)

print(hex(id(woorden)))

woorden2 = woorden.replace('\t', ' - ')
print(woorden)
print("woorden:", hex(id(woorden)))
print(woorden2)
print("woorden2:", hex(id(woorden2)))

print(woorden)
print("woorden:", hex(id(woorden)))
#print(woorden2)


