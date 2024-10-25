setGetallen1 = {1,3,3,3,3,6,6}
print(setGetallen1)

setGetallen2 = {3,6,7}
print(setGetallen2)

print(setGetallen1.difference(setGetallen2))
print(setGetallen1.union(setGetallen2))
print(setGetallen1.intersection(setGetallen2))

lstGetallen = [1,3,3,4,3,4,4,4]
print(lstGetallen)
setGetallen3 = set(lstGetallen)
print(setGetallen3)

print(setGetallen1.union(setGetallen3))
print(setGetallen1.difference(setGetallen3))
#print(setGetallen1[0])

setGetallen1.add(-10)
setGetallen1.add(-100)
setGetallen1.add(10)
setGetallen1.add(-200)
print(setGetallen1)
setGetallen1.add(-1000)
print(setGetallen1)