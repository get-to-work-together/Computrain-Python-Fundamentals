dctData = {}

dctData["Wijnald"] = {}
dctData["Martijn"] = list()
dctData["Ed"] = set()
dctData["Edwin"] = ()


dctData["Wijnald"][(1,2,3)] = 5
dctData["Wijnald"][(1,2,4)] = 6
dctData["Wijnald"][(1,2,5)] = 7

print(dctData)

lstKeys1 = ["A", "B", "C", "D"]
lstValues1 = [1, 2, 3, 4]

temp=zip(lstKeys1, lstValues1)
print(temp)

dctTemp = dict(temp)

print(dctTemp)
