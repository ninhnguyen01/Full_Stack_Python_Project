# Calculating a Running Total

# This program calculates the sum of a series of numbers entered by
# the user.

MAX = 5

# Intialized an accumulator variable.

total = 0.0

# Explain what we are doing.

print('This program calculates the sum of ', end = '')
print(f'{MAX} numbers you will enter.')

# Get the numbers and accumulate them.

for counter in range(MAX): 
    number = int(input('Enter a number: '))
    total = total + number 

# Display the total of the numbers.

print(f'The total is {total}.')

""" The Augmented Assignment Operators """
#  Example +=
