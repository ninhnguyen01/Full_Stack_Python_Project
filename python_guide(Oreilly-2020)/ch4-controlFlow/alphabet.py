vowels = 'aeiou'
letter = input("Enter a letter: ")
if letter in vowels and letter != '':
    print("You entered a vowel")
elif letter not in vowels:
    print("You enterd a consonant or a number")
else:
    print("Something went wrong")