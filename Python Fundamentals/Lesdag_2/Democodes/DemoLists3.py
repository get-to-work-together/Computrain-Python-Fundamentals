codes = ["NL", "B", "L"]

codes.append('F')

print(codes)

codes.extend(['D', 'I'])

print(codes)

codes.insert(1, 'ES')
codes.insert(1, 'ES')
codes.insert(1, 'ES')

print(codes)

code = codes.pop()
print(code)
print(codes)

codes.remove('ES')

print(codes)

codes.sort()

print(codes)

del codes[2]

print(codes)

codes.reverse()

print(codes)