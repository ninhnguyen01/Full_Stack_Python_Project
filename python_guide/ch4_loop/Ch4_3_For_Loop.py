# The 'for' loop: A Count-Controlled Loop 

""" General format for 'for loop' """

# for variable in [value1, value2, etc.]:
# statement
# statement
# etc.

# This program demonstrates a simple 'for' loop
# that uses a list of numbers.
print('I will display the numbers 1 through 5.')
for num in [1,2,3,4,5]:
    print(num)

# This program demonstrates a simple 'for' loop
# that uses a list of numbers.
print('I will display the odd numbers 1 through 9.')
for num in [1,3,5,7,9]:
    print(num)

# This program demonstrates a simple 'for' loop
# that uses a list of strings.
for name in ['Winken', 'Blinken', 'Nod']:
    print(name)

""" Using range Function with the 'for' loop """
for num in range (5):
    print(num)
for num in [1,2,3,4,5]:
    print(num)

# This progam demonstrates how the range loop function can be
# used with a 'for' loop.
# print a message five times.
for x in range (5):
    print('Hello World')

for num in range (1, 5):
    print(num)

for num in range (1,10,2):
    print(num)

""" Using the Target Variable Inside the Loop """
# This program uses a loop to display a table showing the number 
# 1 through 10 and their squares.
# Print the table headings.
print('Number\tSquare')
print('--------------')
# Print the numbers 1 through 10 and their squares.
for number in range (1, 11):
    square = number**2
    print(f'{number}\t{square}')

# This program converts the speeds 60 kph through 130 kph
# (in 10 kph increments) to mph.
START_SPEED = 60 
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

# Print the table headings.
print('KPH\tMPH')
print('--------------')
# Print the Speeds.
for kph in range (START_SPEED,END_SPEED,INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')

""" Letting the User Control the Loop Iterations """
# This program uses a loop to display a table of numbers
# and their squares.
# Get the ending limit.
print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go? '))

# Print the table headings.
print()
print('Number\tsquare')
print('--------------')
# Print the numbers and their squares.
for number in range (1, end + 1):
    square = number **2
    print(f'{number}\t{square}')
    
# This program uses a loop to display a table of numbers
# and their squares.
# Get the starting value.
print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
start = int(input('Enter the starting number: '))
# Get the ending limit.
end = int(input('How high should I go? '))

# Print the table headings.
print()
print('Number\tsquare')
print('--------------')
# Print the numbers and their squares.
for number in range (start, end + 1):
    square = number **2
    print(f'{number}\t{square}')

# Generating an Iterable Sequence that Ranges from Highest to
#  Lowest (section)
for num in range (5, 0, -1):
    print(num)

