# Basic String Operations

""" Iterating over a String with the 'for' Loop """
# General Format:
#   for variable in string:
#       statement
#       statement
#       etc.

name = 'Juliet'
for ch in name:
    print(ch)

# This program counts the number of times the letter T 
# (uppercase or lowercase) appears in a string.
# (with 'for' loop)

def letter_count():
    count = 0
    my_string = input('Enter a sentence: ')
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1
    print(f'The letter T appears {count} times.')

letter_count()

""" Indexing """
my_string = 'Roses are red'
ch = my_string[6]

my_string = 'Roses are red'
print(my_string[0], my_string[6], my_string[10])

# negative numbers
my_string = 'Roses are red'
print(my_string[-1], my_string[-2], my_string[-13])

""" IndexError Exceptions """
# Occur if index out of range for a particular string

city = 'Boston'
index = 0
while index < 6:
    print(city[index])
    index += 1

""" The 'len' Function """
# useful to prevent loops from iterating beyond the end
# of a string. 
city = 'Boston'
size = len(city)
print(size)

city = 'Boston'
index = 0
while index < len(city):
    print(city[index])
    index += 1

""" String Concatenation """

name = 'Kelly'
name += ' '
name += 'Yvonne'
name += ' '
name += 'Smith'
print(name)

""" Strings are immutable """
# This program concatenates strings.
def concat_string():
    name = 'Carmen'
    print(f'The name is: {name}')
    name = name + ' Brown'
    print(f'Now the name is: {name}')

concat_string()

# no string[index] on left side of an assignment operator
# Error below
friend = 'Bill'
# friend[0] = 'J'
