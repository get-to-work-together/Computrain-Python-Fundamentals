lst = [x**2 for x in range(10)]

print(lst)

lst2 = []
for x in range(10):
    lst2.append(x**2)

print(lst2)

lst3 = [i*i for i in range(10) if i > 5]

print(lst3)

lst4 = []
for i in range(10):
    if i > 5:
        lst4.append(i*i)

print(lst4)