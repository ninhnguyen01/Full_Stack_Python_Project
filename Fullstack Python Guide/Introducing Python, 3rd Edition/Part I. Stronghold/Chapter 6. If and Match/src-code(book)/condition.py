# control flow:

# Equality ==
# Inequality !=
# Less than <
# Less than or equal <=
# Greater than >
# Greater than or equal >=

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")

color = "mauve"
if color == "red":
   print("It's a tomato")
elif color == "green":
   print("It's a green pepper")
elif color == "bee purple":
   print("I don't know what it is, but only bees can see it")
else:
   print("I've never heard of the color", color)

some_list = []
if some_list:
     print("There's something in here")
else:
     print("Hey, it's empty!")

letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
     or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

vowels = 'aeiou'
letter = 'o'
letter in vowels

if letter in vowels:     
    print(letter, 'is a vowel')

letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set)

vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list)

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple)

vowel_dict = {'a': 'apple', 'e': 'elephant',
               'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
print(letter in vowel_dict)

vowel_string = "aeiou"
print(letter in vowel_string)
