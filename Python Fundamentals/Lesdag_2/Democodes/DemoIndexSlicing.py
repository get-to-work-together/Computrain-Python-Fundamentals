import string
letters = list(string.ascii_letters)

print(letters[0])

print(letters[0:3])

print(letters[-5:-2])

print(letters[0:20:2])

print(letters[::-1])

lstGetallen = [1,2,3]

lstAlles = lstGetallen + letters

print(lstAlles)
print(lstGetallen)
print(letters)

print(letters.index("k"))

g1, g2, g3 = lstGetallen

print(g1)