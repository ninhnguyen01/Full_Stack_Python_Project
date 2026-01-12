# Calculating a Running Total (Title)

# The Augmented Assignment Operators 
""" variable += expression (variable = variable + expression) """

# This program calculates the sum of a series of numbers entered by
# the user.
MAX = 5

# Intialized an accumulator variable.
total = 0.0
# 4.13 What is an accumulator?
""" A variable that is used to accumulate the total of a series of numbers. """
# 4.14 Should an accumulator be initialized to any specific value?
# Why or why not?
""" The accumulator should be initialized to a 0 or else it will
not contain the correct total of numbers when the loop ends. """

# Explain what we are doing.
print('This program calculates the sum of ', end = '')
print('f{MAX} numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(MAX): 
    number = int(input('Enter a number: '))
    total += number 

# Display the total of the numbers.
print(f'The total is {total}.')
