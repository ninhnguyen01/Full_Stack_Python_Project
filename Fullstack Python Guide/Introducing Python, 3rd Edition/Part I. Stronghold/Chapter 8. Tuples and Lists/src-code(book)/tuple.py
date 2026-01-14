one_marx = 'Groucho',
print(one_marx)

# You could enclose them in parentheses and still get the same tuple:
one_marx = ('Groucho',)
print(one_marx)

# Here’s a little gotcha: if you have a single thing in parentheses and omit that comma, 
# you would not get a tuple, but just the thing (in this example, the string Groucho):
one_marx = ('Groucho')
print(one_marx)

print(type(one_marx))

# If you have more than one element, follow all but the last one with a comma:
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

# Actually, having a comma after the last element doesn’t hurt (some languages are more picky about this):
marx_tuple = 'Groucho', 'Chico', 'Harpo',
print(marx_tuple)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

one_marx = 'Groucho',
print(type(one_marx))

print(type('Groucho',))

print(type(('Groucho',)))

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))
print(tuple('abc'))
print(tuple(b'\x01\x02\x03'))

t = 1, 2, 3
print(t[0])

print(('Groucho',) + ('Chico', 'Harpo'))

print(('yada',) * 3)

words = ('fresh','out', 'of', 'ideas')
for word in words:
    print(word)

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop,')
print(t1 + tuple(t2))

# This means that you can appear to modify a tuple like this:
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop,')
t1 += tuple(t2)
print(t1)

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1 += t2
print(id(t1))
