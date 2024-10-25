l1 = ['one','two','three','four']
l1_sorted = sorted(l1, key = len)
print(l1_sorted)

l2 = [23, 45, 56, 38, 59, 82, 75]
l2_filtered = filter(lambda x: x%5 == 0, l2)
print(l2_filtered)
for li in l2_filtered:
    print(li)

l3_mapped = map(lambda x: x**3, range(10))
print(l3_mapped)
for li in l3_mapped:
    print(li)