# To get a single character from a string, specify its offset inside square brackets after the string’s name. 
# The first (leftmost) offset is 0, the next is 1, and so on. 
# The last (rightmost) offset can be specified with –1 so you don’t have to count; going to the left are –2, –3, and so on:

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[25])
print(letters[0])

# From offset 4 to 19, by 3:
print(letters[4:20:3])

# The len() function counts characters in a string:
print(len(letters))
