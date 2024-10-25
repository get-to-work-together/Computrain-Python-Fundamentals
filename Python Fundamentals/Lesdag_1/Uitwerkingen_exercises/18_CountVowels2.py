text = input("Write some text: ")
numberOfCharacters = len(text)
vowels = "aeiouy"

numberOfVowels = 0
for vowel in vowels:
    aantalKlinkers = text.count(vowel)

    print("Found the vowel ", vowel, " ", aantalKlinkers, " time(s).")
    numberOfVowels = numberOfVowels + aantalKlinkers

print("The complete text contains ", numberOfCharacters, " character(s).")
print("The text contains ", numberOfVowels, " vowel(s).")

