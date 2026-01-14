# To create a non-empty set, use {} with values, or use the set() function with an iterable argument 
# (a tuple, list, string, or dict):
evens = {0, 2, 4, 6, 8}
print(evens)

evens = set( [0, 2, 4, 6, 8] )
print(evens)

evens = set( (0, 2, 4, 6, 8) )
print(evens)

evens = set( {0:1, 2:4, 4:8, 6:12, 8:16} )
print(evens)

# Sets contain unique values, so any duplicates are dropped:
print(set( 'letters' ))

reindeer = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
print(len(reindeer))

# Add an Item with add()
# Throw another item into a set with the set add() method:
s = set((1,2,3))
print(s)

s = s.add(4)
print(s)

# If you try to add something that was already in there, no problem:
s = set((1,2,3))
s = s.add(2)
print(s)

s = set((1,2,3))
s.remove(3)
print(s)

a = set((1, 3, 5))
b = set((2, 4, 6))
print(a | b)

furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
        'cream' in contents):
        print(name)

# Let’s use the set intersection operator, which is an ampersand (&):
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

print(a & b)

print(a.intersection(b))

print(bruss & wruss)

print(a | b)

print(a.union(b))

print(bruss | wruss)

print(a - b)

print(a.difference(b))

print(bruss - wruss)

print(wruss - bruss)

print(a ^ b)

print(a.symmetric_difference(b))

print(bruss ^ wruss)

# You can check whether one set is a subset of another (all members of the first set are also in the second set) 
# by using <= or issubset():
print(a <= b)

print(a.issubset(b))

print(bruss <= wruss)

# Is any set a subset of itself? Yup:
print(a <= a)

print(a.issubset(a))

print(a < b)

print(a < a)

print(bruss < wruss)

print(a >= b)

print(a.issuperset(b))

print(wruss >= bruss)

# Any set is a superset of itself:
print(a >= a)

print(a.issuperset(a))

print(a > b)

print(wruss > bruss)

print(a > a)

# The simplest version looks like the list and dictionary comprehensions that you’ve just seen:
#     { expression for expression in iterable }
# And it can have the optional condition tests:
#     { expression for expression in iterable if condition }

a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

frozenset([3, 2, 1])
frozenset({1, 2, 3})
frozenset(set([2, 1, 3]))
frozenset({1, 2, 3})
frozenset({3, 1, 2})
frozenset({1, 2, 3})
frozenset( (2, 3, 1) )
frozenset({1, 2, 3})

fs = frozenset([3, 2, 1])
print(fs)
