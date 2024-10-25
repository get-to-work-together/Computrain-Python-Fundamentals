text = input("Write some text: ")
numberOfCharacters = len(text)
vowels = "aeiouy"
#vowels = ["a", "e", "i", "o", "u","y"]

numberOfVowels = 0
for vowel in vowels:
    aantalKlinkers = 0
    for letter in text:
        #print("letter:", letter, "vowel:", vowel)
        if letter == vowel:
            aantalKlinkers = aantalKlinkers + 1

    print("Found the vowel ", vowel, " ", aantalKlinkers, " time(s).")
    numberOfVowels = numberOfVowels + aantalKlinkers

print("The complete text contains ", numberOfCharacters, " character(s).")
print("The text contains ", numberOfVowels, " vowel(s).")

