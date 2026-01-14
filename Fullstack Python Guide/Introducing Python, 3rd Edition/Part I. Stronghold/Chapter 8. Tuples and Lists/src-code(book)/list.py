# List data type
empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]

# The simplest form of list comprehension looks like this:
# [expression for item in iterable]
# A list comprehension can include a conditional expression, looking something like this:
# [expression for item in iterable if condition]

# turn string 'cat' to a list
print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

talk_like_a_pirate_day = '9/19/2024'
print(talk_like_a_pirate_day.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('//'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])


marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])

print(marxes[::2])

# Here, we start at the end and go left by 2:
print(marxes[::-2])

# And finally, here’s a trick to reverse a list:

print(marxes[::-1])

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.reverse())

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.append('Zeppo'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.insert(2, 'Gummo'))
print(marxes.insert(10, 'Zeppo'))

print(["blah"] * 3)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
print(marxes.extend(others))

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)


numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])

del marxes[-1]
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()
print(marxes)
marxes.pop(1)
print(marxes)

work_quotes = ['Working hard?', 'Quick question!', 'Number one ']
print(work_quotes)

work_quotes.clear()
print(work_quotes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)

print('Bob' in marxes)

words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))

print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)

separated = joined.split(separator)
print(separated)
print(separated == friends)

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)

marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
print(numbers.sort())

numbers = [2, 1, 4.0, 3]
print(numbers.sort(reverse=True))

marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

a = [1, 2, 3]
print(a)

b = a
print(b)
[1, 2, 3]

a[0] = 'surprise'
print(a)

print(b)

print(b)

b[0] = 'I hate surprises'
print(b)

print(a)

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)

a[2][1] = 10
print(a)
print(b)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
     print(cheese)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
     if cheese.startswith('g'):
         print("I won't eat anything that starts with 'g'")
         break
     else:
         print(cheese)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
     if cheese.startswith('x'):
         print("I won't eat anything that starts with 'x'")
         break
     else:
         print(cheese)
else:
    print("Didn't find anything that started with 'x'")

cheeses = []
for cheese in cheeses:
     print('This shop has some lovely', cheese)
     break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
     print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list(zip(english, french)))

print(dict(zip(english, french)))

from itertools import zip_longest
a = [1, 2, 3]
b = [1, 2, 3, 4, 5]
for x in zip(a, b):
     print(x)

for x in zip_longest(a, b):
     print(x)

for x in zip_longest(a, b, fillvalue='!'):
     print(x)

number_list = []
for number in range(1, 6):
     number_list.append(number)

print(number_list)

number_list = list(range(1, 6))
print(number_list)

number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)

a_list = []
for number in range(1,6):
     if number % 2 == 1:
         a_list.append(number)
         print(a_list)

rows = range(1,4)
cols = range(1,3)
for row in rows:
     for col in cols:
         print(row, col)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]

for cell in cells:
     print(cell)

for row, col in cells:
     print(row, col)

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds)

print(all_birds[0])
['hummingbird', 'finch']

print(all_birds[1])

print(all_birds[1][0])
