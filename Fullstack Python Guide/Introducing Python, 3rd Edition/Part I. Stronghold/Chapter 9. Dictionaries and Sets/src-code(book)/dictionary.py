# Ambrose Bierce’s The Devil’s Dictionary:
# Dictionary data type
bierce = {
     "day": "A period of twenty-four hours, mostly misspent",
     "positive": "Mistaken at the top of one's voice",
     "misfortune": "The kind of fortune that never misses",
     }

print(bierce)

acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)

acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
dict(lol)
{'a': 'b', 'c': 'd', 'e': 'f'}

# A list of two-item tuples:
lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
dict(lot)
{'a': 'b', 'c': 'd', 'e': 'f'}

# A tuple of two-item lists:
tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
dict(tol)
{'a': 'b', 'c': 'd', 'e': 'f'}

# A list of two-character strings:
los = [ 'ab', 'cd', 'ef' ]
dict(los)
{'a': 'b', 'c': 'd', 'e': 'f'}

tos = ( 'ab', 'cd', 'ef' )
dict(tos)
{'a': 'b', 'c': 'd', 'e': 'f'}

pythons = {
     'Chapman': 'Graham',
     'Cleese': 'John',
     'Idle': 'Eric',
     'Jones': 'Terry',
     'Palin': 'Michael',
     }

print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
     'Graham': 'Chapman',
     'John': 'Cleese',
     'Eric': 'Idle',
     'Terry': 'Gilliam',
     'Michael': 'Palin',
     'Terry': 'Jones',
     }

print(some_pythons)

print(some_pythons['John'])

print('Groucho' in some_pythons)

print(some_pythons.get('John'))

print(some_pythons.get('Groucho', 'Not a Python'))

print(some_pythons.get('Groucho'))

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
               'person': 'Col. Mustard'}

for card in accusation:
     print(card)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
     'person': 'Col. Mustard'}

for card in accusation.keys():
     print(card)

card_list = list(accusation.keys())
print(card_list)

for value in accusation.values():
     print(value)

for item in accusation.items():
     print(item)

for card, contents in accusation.items():
     print('Card', card, 'has the contents', contents)

pythons = {
     'Chapman': 'Graham',
     'Cleese': 'John',
     'Gilliam': 'Terry',
     'Idle': 'Eric',
     'Jones': 'Terry',
     'Palin': 'Michael',
     }

print(pythons)

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }


print(pythons.update(others))

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
print(first.update(second))

# Starting with version 3.5, Python has a new way to merge dictionaries, 
# using the ** unicorn glitter (or dictionary unpacking), which has a very different use in Chapter 10:
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
{**first, **second}
{'a': 'agony', 'b': 'bagels', 'c': 'candy'}

# You can pass more than two dictionaries:
third = {'d': 'donuts'}
{**first, **third, **second}
{'a': 'agony', 'b': 'bagels', 'd': 'donuts', 'c': 'candy'}

# Use |
# Python 3.9 added the ability to use the operator |. Adapting one of the earlier examples, we can use | as follows:
first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
print(first | second)
print(first)

first |= second
print(first)

del pythons['Marx']
print(pythons)

del pythons['Howard']
print(pythons)

print(len(pythons))

pythons.pop('Palin')

print(len(pythons))

print(pythons.pop('First', 'Hugo'))

print(len(pythons))

print(pythons.clear())

pythons = {}
print(pythons)

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
 'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}

print('Chapman' in pythons)

print('Palin' in pythons)

print('Gilliam' in pythons)

signals = {'green': 'go',
 'yellow': 'go faster',
 'red': 'smile for the camera'}

save_signals = signals

signals['blue'] = 'confuse everyone'

print(save_signals)

signals = {'green': 'go',
 'yellow': 'go faster',
 'red': 'smile for the camera'}

original_signals = signals.copy()

signals['blue'] = 'confuse everyone'

print(signals)

print(original_signals)

signals = {'green': 'go',
 'yellow': 'go faster',
 'red': ['stop', 'smile']}

signals_copy = signals.copy()

print(signals)

print(signals_copy)

signals['red'][1] = 'sweat'

print(signals)

print(signals_copy)

import copy

signals = {'green': 'go',
 'yellow': 'go faster',
 'red': ['stop', 'smile']}

signals_copy = copy.deepcopy(signals)

print(signals)

print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)

print(signals_copy)

# dictionaries also have comprehensions. The simplest form looks familiar:
# {key_expression : value_expression for expression in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# dictionary comprehensions can also have if tests and multiple for clauses:
# {key_expression : value_expression for expression in iterable if condition}
vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)
