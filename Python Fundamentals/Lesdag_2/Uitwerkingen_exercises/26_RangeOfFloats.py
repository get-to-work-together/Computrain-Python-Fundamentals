def drange(start, stop, step=1.0, endpoint=False):
    lstFloats = [number + step for number in range(start,stop+endpoint)]
    return lstFloats

print(drange(1,10))

print(drange(1,13))

print(drange(2,13, 2,endpoint=True))

print(drange(2,13, 0.1,endpoint=True))