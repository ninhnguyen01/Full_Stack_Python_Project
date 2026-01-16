from collections import defaultdict, Counter, OrderedDict
import itertools
from random import choice
from random import sample
from random import randint
from random import randrange
from random import random

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

# If the key is not already in the dictionary, the new value is used:
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

# If we try to assign a different default value to an existing key, the original value is returned and nothing is changed:
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

# The defaultdict() function is similar but specifies the default value for any new key up front, when the dictionary is created. Its argument is a function. In this example, we pass the function int, which will be called as int() and return the integer 0:
periodic_table = defaultdict(int)

# Now any missing value will be an integer (int) with the value 0:
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

# The argument to defaultdict() is a function that returns the value to be assigned to a missing key. In the following example, no_idea() is executed to return a value when needed:
def no_idea():
     return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

# You can use the functions int(), list(), or dict() to return default empty values for those types: int() returns 0, list() returns an empty list ([]), and dict() returns an empty dictionary ({}). If you omit the argument, the initial value of a new key will be set to None.
# By the way, you can use lambda to define your default-making function right inside the call:
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

# Using int is one way to make your own counter:
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
     food_counter[food] += 1

for food, count in food_counter.items():
     print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
     if not food in dict_counter:
         dict_counter[food] = 0
     dict_counter[food] += 1

for food, count in dict_counter.items():
     print(food, count)

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))
print(breakfast_counter)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)

quotes = {
     'Moe': 'A wise guy, huh?',
     'Larry': 'Ow!',
     'Curly': 'Nyuk nyuk!',
     }

for stooge in quotes:
  print(stooge)

quotes = OrderedDict([
     ('Moe', 'A wise guy, huh?'),
     ('Larry', 'Ow!'),
     ('Curly', 'Nyuk nyuk!'),
     ])

for stooge in quotes:
     print(stooge)

def palindrome(word):
     from collections import deque
     dq = deque(word)
     while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
     return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

def another_palindrome(word):
     return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))

for item in itertools.chain([1, 2], ['a', 'b']):
     print(item)

for item in itertools.cycle([1, 2]):
     print(item)

for item in itertools.accumulate([1, 2, 3, 4]):
     print(item)

def multiply(a, b):
     return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
     print(item)

print(choice([23, 9, 46, 'bacon', 0x123abc]))
print(choice( ('a', 'one', 'and-a', 'two') ))
print(choice(range(100)))
print(choice('alphabet'))

print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
print(sample(('a', 'one', 'and-a', 'two'), 2))
print(sample(range(100), 4))
print(sample('alphabet', 7))

print(randint(38, 74))
print(randint(38, 74))
print(randint(38, 74))

print(randrange(38, 74))
print(randrange(38, 74, 10))
print(randrange(38, 74, 10))

print(random())
print(random())
print(random())
