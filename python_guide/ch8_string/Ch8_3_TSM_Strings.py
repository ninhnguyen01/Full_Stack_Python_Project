# Testing, Searching, and Manipulating Strings

""" Testing strings with 'in' and 'not' in """
# General Format:
# string1 in string2

text = 'Four score and seven years ago'
if 'seven' in text:
    print('The string "seven" was found.')
else:
    print('The string "seven" was not found.')

names = 'Bill Joanne Susan Chris Juan Katie'
if 'Pierre' not in names:
    print('Pierre was not found.')
else:
    print('Pierre was found.')

""" String Methods """
# test value of strings
# perform mods
# search substrings and replace sequences of characters

# General Format:
# stringvar.method(arguments)

# String Testing Methods
string1 = '1200'
if string1.isdigit():
    print(f'{string1} contains only digits.')
else:
    print(f'{string1} contains characters other than digits.')

# string test methods
# isalnum()
# isalpha()
# isdigit()
# islower()
# isspace()
# issupper()

# This program demonstrates several testing methods.
def main():
    user_string = input('Enter a string: ')
    print('This is what I found about that string: ')
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only white space characters')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

if __name__ == '__main__':
    main()

# string mod methods
# lower()
# lstrip()
# lstrip(char)
# rstrip()
# rstrip(char)
# strip()
# strip(char)
# upper()

""" Modification Methods """
letters = 'WXYZ'
print(letters, letters.lower())

letters = 'abcd'
print(letters, letters.upper())

again = 'y'
while again.lower() == 'y':
    print('Hello')
    print('Do you want to see that again?')
    again = input('y = yes, anything else = no: ')

while again.upper() == 'Y':
    print('Hello')
    print('Do you want to see that again?')
    again = input('y = yes, anything else = no: ')

""" Searching and Replacing """

# search and replace methods
# endswith(substring)
# find(substring)
# replace(old,new)
# startswith(substring) 

filename = input('Enter the filename: ')
if filename.endswith('.txt'):
    print('That is the name of a text file.')
elif filename.endswith('.py'):
    print('That is the name of a Python source file.')
elif filename.endswith('.doc'):
    print('that is the name of a word processing document.')
else:
    print('Unknown file type.')

string = 'Four score and seven years ago'
position = string.find('seven')
if position != '-1':
    print(f'The word "seven" was found at index {position}.')
else:
    print('The word "seven" was not found.')  
 
string = 'Four score and seven years ago'
new_string = string.replace('years','days')
print(new_string)

# see login.py
# see validate_password.py

""" Repetition Operator """
# General format:
# string_to_copy * N

my_string = 'w' * 5 
print(my_string)

def count():
    for count in range(1,10):
        print('Z' * count)
    
    for count in range(8,0,-1):
        print('Z' * count)

count()

""" Splitting a String """
# This program demonstrates the split method.
def split_text():
    my_string = 'One two three four'
    word_list = my_string.split()
    print(word_list)

split_text()

# This program calls the split method, using the '/' character
# as a separator.
def date_split():
    date_string = '11/26/2020'
    date_list = date_string.split('/')
    print(f'Month: {date_list[0]}')
    print(f'Day: {date_list[1]}')
    print(f'Year: {date_list[2]}')

date_split()

# This program demonstrates how to tokenize strings.
# see tokens.py

