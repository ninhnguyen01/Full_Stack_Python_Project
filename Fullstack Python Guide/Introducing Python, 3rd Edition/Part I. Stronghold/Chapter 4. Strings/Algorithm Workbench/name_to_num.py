# This program I wrote goes beyond the scope of this chapter

# 26 letters in the English Alphabet
LETTERS = 'abcdefghijklmnopqrstuvwxyz' # first index is 0

# Dictionary of alphabet, number pair
alphabet_num = {'a': 1, 'b': 2 ,'c': 3,'d': 4,'e': 5,\
                'f': 6,'g': 7,'h': 8, 'i': 9, 'j': 10,\
                    'k': 11,'l': 12, 'm': 13, 'n': 14,'o': 15,\
                        'p': 16, 'q': 17, 'r': 18, 's': 19,'t': 20,\
                            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,\
                                'z': 26}

while True:
    # Find the corresponding alphabet, number pair
    print('-' * 30) # create border line
    print()

    print("[ Type q to quit ]")
    # user input and converting uppercase entry to lowercase
    enter_name = input("Enter a name (first or last): ").lower() 
    if enter_name == 'q':
        break
    print("Name:", enter_name)
    # pair the variables with 'zip'
    for name_letter, num in zip(enter_name, alphabet_num):
        if name_letter in alphabet_num:
            # look for key "letter" to return value "number"
            print(f"Letter: {name_letter} | Number: {alphabet_num[name_letter]}") 

    print()
    print('-' * 30) # create border line
    print()
