text = input("Write some text: ")

dctVowelCount = {}

for letter in text:
    #print(letter)

    if letter in dctVowelCount.keys():
        dctVowelCount[letter] += 1
    else:
        dctVowelCount[letter] = 1

lstAllVowels = sorted(dctVowelCount.keys())

numberOfCharacters = 0
numberOfVowels = 0
for letter in lstAllVowels:
    print("Found the vowel ", letter, " ", dctVowelCount[letter], " time(s).")
    numberOfCharacters += dctVowelCount[letter]
    numberOfVowels += 1

print("The complete text contains ", numberOfCharacters, " character(s).")
print("The text contains ", numberOfVowels, " vowel(s).")

