text = input("Give some text: ")

text = text.lower().replace(".", "").replace(",","")
lstText = text.split()
print(lstText)

setUniqueWords = set(lstText)

print(setUniqueWords)
dctUniqueWordCount = {}

for uniqueWord in setUniqueWords:
    print(uniqueWord)
    dctUniqueWordCount[uniqueWord] = lstText.count(uniqueWord)

print(dctUniqueWordCount)

for word, n in dctUniqueWordCount.items():
    print(word, n)