# Why have two kinds of quote characters? 
# The main purpose is to create strings containing quote characters. 
# You can have single quotes inside double-quoted strings, or double quotes inside single-quoted strings:

print("'Nay!' said the naysayer. 'Neigh?' said the horse.")
print('The rare double quote in captivity: ".')
print('A "two by four" is actually 1 1/2" * 3 1/2".')
print("'There's the man that shot my paw!' cried the limping hound.")

# You can also use three single quotes (''') or three double quotes ("""):
print('''Boom!''')
print("""Eek!""")

# Triple quotes aren’t very useful for short strings like these. 
# Their most common use is to create multiline strings, like this classic poem from Edward Lear:
poem = '''There was a Young Lady of Norway,
... Who casually sat in a doorway;
... When the door squeezed her flat,
... She exclaimed, "What of that?"
... This courageous Young Lady of Norway.'''

print(poem)

# The print() function strips quotes from strings and prints their contents. 
# This function is meant for human output. 
# It helpfully adds a space between each of the elements it prints, and a newline at the end:
print('Give', "us", '''some''', """space""")
