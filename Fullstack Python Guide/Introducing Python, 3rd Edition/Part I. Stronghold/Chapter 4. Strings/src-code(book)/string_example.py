# Python has a large set of string functions. 
# Let’s explore how the most common of them work. 
# Our test subject is the following string containing the text of the immortal poem 
# “What Is Liquid?” by Margaret Cavendish, Duchess of Newcastle:

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))

# Python has two methods, find() and index(), for finding the offset of a substring, 
# and has two versions of each (starting from the beginning or the end). 
# They work the same if the substring is found. 
# If it isn’t, find() returns -1, and index() raises an exception.
word = 'the'
print(poem.find(word))
print(poem.index(word))

# And the offset of the last the:
word = 'the'
print( poem.rfind(word))
print( poem.rindex(word))

print(poem.count(word))

# Are all the characters in the poem either letters or numbers?
print(poem.isalnum())

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
