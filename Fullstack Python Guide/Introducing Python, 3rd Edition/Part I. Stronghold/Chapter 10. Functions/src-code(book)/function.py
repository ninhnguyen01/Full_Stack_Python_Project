def do_nothing():
    pass # to prevent error and do later

def make_a_sound():
    print('quack')

make_a_sound()

# Let’s try a function that has no parameters but returns a value:
def agree():
  return True

# You can call this function and test its returned value by using if:

if agree():
   print('Splendid!')
else:
   print('That was unexpected.')

def echo(anything):
  return anything + ' ' + anything

# Now let’s call echo() with the string Rumplestiltskin:
echo('Rumplestiltskin')

def commentary(color):
   if color == 'red':
       return "It's a tomato."
   elif color == "green":
       return "It's a green pepper."
   elif color == 'bee purple':
       return "I don't know what it is, but only bees can see it."
   else:
       return "I've never heard of the color "  + color +  "."

comment = commentary('blue')
print(comment)


thing = None
print(bool(thing))

if thing:
   print("It's some thing")
else:
   print("It's no thing")

thing = None
if thing is None:
   print("It's nothing")
else:
   print("It's something")

thing = 0
print(bool(thing))
print(thing == False)
print(thing is False)

thing = 1
print(bool(thing))
print(thing == True)
print(thing is True)

def whatis(thing):
   if thing is None:
       print("None")
   elif thing:
       print("true")
   else:
       print("false")

whatis(None)
whatis(True)
whatis(False)

def menu(wine, entree, dessert):
   return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))


def menu(wine, entree, dessert='pudding'):
   return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))

def buggy(arg, result=[]):
   result.append(arg)
   print(result)

buggy('a')
buggy('b')   # expect ['b']

def works(arg):
   result = []
   result.append(arg)
   return result

works('a')
works('b')

def nonbuggy(arg, result=None):
   if result is None:
       result = []
   result.append(arg)
   print(result)

nonbuggy('a')
nonbuggy('b')

def print_args(*args):
   print('Positional tuple:', args)

print_args()

# Whatever you give it will be printed as the args tuple:
print_args(3, 2, 1, 'wait!', 'uh')

def print_more(required1, required2, *args):
   print('Need this one:', required1)
   print('Need this one too:', required2)
   print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
print_args(2, 5, 7, 'x')

args = (2,5,7,'x')
print_args(args)

print_args(*args)

def print_kwargs(**kwargs):
   print('Keyword arguments:', kwargs)

print_kwargs()

# You may want an argument to be in a defined position, and that requires the use of a single slash (/) 
# just after the position-only parameters:
""" def print_data(data, /, start=0, end=100):
   for value in (data[start:end]):
       print(value)

print_data(data, 2, 4)

print_data(data, end=5, start=3) """


# First, let’s define a function that takes an iterable data argument and optional start and end indices:
def print_data(data, start=0, end=100):
   for value in (data[start:end]):
       print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']

# We could call the arguments out of order by passing them all as keyword arguments:
print_data(start=0, end=4, data=data)

def print_data(data, *, start=0, end=100):
   for value in (data[start:end]):
       print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']

print_data(data, start=0, end=4)
print_data(data, start=4)
print_data(data, end=2)

outside = ['one', 'fine', 'day']
def mangle(arg):
  arg[1] = 'terrible!'

print(outside)

mangle(outside)
print(outside)

def echo(anything):
   'echo returns its input argument'
   return anything

# You can make a docstring quite long, and even add rich formatting if you want:
def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

# To test this, let’s define a simple function called answer() that doesn’t have any arguments; it just prints the number 42:
def answer():
   print(42)

# If you run this function, you know what you’ll get:
answer()

# Now let’s define another function named run_something. It has one argument called func, a function to run. Once inside, it just calls the function:

def run_something(func):
   func()

run_something(answer)

def outer(a, b):
   def inner(c, d):
       return c + d
   return inner(a, b)

outer(4, 7)

def knights(saying):
   def inner(quote):
       return f"We are the knights who say: '{quote}'"
   return inner(saying)

knights('Ni!')

def knights2(saying):
   def inner2():
       return "We are the knights who say: '%s'" % saying
   return inner2

# Let’s call knights2() twice, with different arguments:
a = knights2('Duck')
b = knights2('Hasenpfeffer')

# If we call them, they remember the saying that was used when they were created by knights2:
print(a())
print(b())


stairs = ['thud', 'meow', 'thud', 'hiss']
# And for the function, let’s use one that will capitalize each word and append an exclamation point, perfect for feline tabloid newspaper headlines:
def enliven(word):   # give that prose more punch
   return word.capitalize() + '!'

# Then we mix our ingredients:
# Finally, we get to the lambda. The enliven() function is so brief that we can replace it with a lambda:
def my_range(first=0, last=10, step=1):
   number = first
   while number < last:
       yield number
       number += step

def my_range(first=0, last=10, step=1):
   def inner():
        number = first
        while number < last:
            yield number
            number += step
   return inner

ranger = my_range(1, 5)
for x in ranger():
   print(x)
for x in ranger():
   print(x)

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)

for thing in genobj:
   print(thing)

# Here’s what the code looks like:
def document_it(func):
   def new_function(*args, **kwargs):
       print('Running function:', func.__name__)
       print('Positional arguments:', args)
       print('Keyword arguments:', kwargs)
       result = func(*args, **kwargs)
       print('Result:', result)
       return result
   return new_function

def add_ints(a, b):
  return a + b

add_ints(3, 5)

cooler_add_ints = document_it(add_ints)  # manual decorator assignment
print(cooler_add_ints(3, 5))

@document_it
def add_ints(a, b):
   return a + b

add_ints(3, 5)

def square_it(func):
   def new_function(*args, **kwargs):
       result = func(*args, **kwargs)
       return result * result
   return new_function

# The decorator that’s used closest to the function (just above the def) runs first and then the one above it. 
# Either order gives the same end result, but you can see how the intermediate steps change:
@document_it
@square_it
def add_ints(a, b):
   return a + b

add_ints(3, 5)

# Let’s try reversing the decorator order:
@square_it
@document_it
def add_ints(a, b):
   return a + b

add_ints(3, 5)

from functools import wraps
# def outer():
#    @wraps(func)
#    def inner(*args, **kwargs):
#        pass
#    return inner

animal = 'fruitbat'
def print_global():
   print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

def change_local():
   animal = 'wombat'
   print('inside change_local:', animal, id(animal))

change_local()

print(animal)
print(id(animal))

animal = 'fruitbat'
def change_and_print_global():
   global animal
   animal = 'wombat'
   print('inside change_and_print_global:', animal)

print(animal)
change_and_print_global()

print(animal)

# And here they are in use:
animal = 'fruitbat'
def change_local():
   animal = 'wombat'  # local variable
   print('locals:', locals())

print(animal)
change_local()

print('globals:', globals()) # reformatted a little for presentation
print(animal)

def amazing():
   '''This is the amazing function.
   Want to see it again?'''
   print('This function is named:', amazing.__name__)
   print('And its docstring is:', amazing.__doc__)

amazing()

def flatten(lol):
   for item in lol:
       if isinstance(item, list):
           for subitem in flatten(item):
               yield subitem
       else:
           yield item

lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
flatten(lol)

list(flatten(lol))

def flatten(lol):
   for item in lol:
       if isinstance(item, list):
           yield from flatten(item)
       else:
           yield item

lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
list(flatten(lol))

short_list = [1, 2, 3]
position = 5
try:
   short_list[position]
except:
   print('Need a position between 0 and', len(short_list)-1, 'but got',
          position)

# You get the full exception object in the variable name if you use this form:
# except exceptiontype as name
short_list = [1, 2, 3]
while True:
   value = input('Position [q to quit]? ')
   if value == 'q':
       break
   try:
       position = int(value)
       print(short_list[position])
   except IndexError:
       print('Bad index:', position)
   except Exception as other:
       print('Something else broke:', other)

try:
   100 / 0
   print("I don't know how I did this.")
except ZeroDivisionError:
   print("Really?")
finally:
   print("Can life go on now?")
