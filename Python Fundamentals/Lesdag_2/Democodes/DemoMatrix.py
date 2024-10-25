matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

print(matrix1)
print(matrix1[0])

print(matrix1[1][1])

# Matrix vermenigvuldigen:

for ri in range(len(matrix1)):
    for ci in range(len(matrix1[ri])):
        matrix1[ri][ci] = matrix1[ri][ci] * 2

print(matrix1)