vowels = 'aeiou'
letter = input("Enter a single letter: ")
if letter.lower() in vowels:
    print(letter, "is a vowel.")
else:
    print("You entered a consonant!")