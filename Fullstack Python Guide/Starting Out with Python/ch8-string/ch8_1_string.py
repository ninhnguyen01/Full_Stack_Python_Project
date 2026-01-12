# Basic String Operations (Title)

# Iterating over a String with the 'for' Loop 
""" General Format:
    for variable in string:
        statement
        statement
        etc. """

# The 'len' Function 
# useful to prevent loops from iterating beyond the end
# of a string. 

# 8.2 What is the index of the first character in a string?
""" 0 """

# 8.3 If a string has 10 characters, what is the index of the 
# last character?
""" 9 """

# 8.4 What happeneds if you try to use an invalid index to
# access a character in a string?
""" An IndexError exception will occur if you try to use an 
index that is out of range for a particular string. """
 
# 8.5 How do you find the length of a string?
""" Use the built-in len function. """

""" The second statement attempts to assign a value to an 
individual character in the string. Strings are immutable,
however, so the expression animal [0] cannot appear on the
left side of an assignment operator. """

name = 'Juliet'
for ch in name:
    print(ch)

# This program counts the number of times the letter T 
# (uppercase or lowercase) appears in a string.
# (with 'for' loop)
def main():
    count = 0
    my_string = input('Enter a sentence: ')
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1
    print(f'The letter T appears {count} times.')

if __name__ == '__main__':
    main()

# Indexing 
my_string = 'Roses are red'
ch = my_string[6]

my_string = 'Roses are red'
print(my_string[0], my_string[6], my_string[10])

# negative numbers
my_string = 'Roses are red'
print(my_string[-1], my_string[-2], my_string[-13])

# IndexError Exceptions 
# Occur if index out of range for a particular string
# city = 'Boston'
# print(city[6])

# city = 'Boston'
# index = 0
# while index < 7:
#     print(city[index])
#     index += 1

city = 'Boston'
size = len(city)
print(size)

city = 'Boston'
index = 0
while index < len(city):
    print(city[index])
    index += 1

# String Concatenation 
name = 'Kelly'
name += ' '
name += 'Yvonne'
name += ' '
name += 'Smith'
print(name)

# Strings are immutable 
# This program concatenates strings.
def main2():
    name = 'Carmen'
    print(f'The name is: {name}')
    name = name + ' Brown'
    print(f'Now the name is: {name}')

if __name__ == '__main__':
    main2()
