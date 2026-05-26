# Introduction to Value-Returning Functions: Generating Random
# Numbers (Title)

# Reading

# Import Statement Example
import math

# Generating Random Numbers (section)
import random

# randit function
number = random.randint (1,100)

# This program displays a random number in the range 1 through 10
import random
def main():
    number = random.randint(1,10)
    print(f'The number is {number}.')

main()

import random
def main():
    for count in range (5):
        number = random.randint(1,10)
        print(number)

main()

print(random.randint(1,10))

import random
def main():
    for count in range (5):
        print(random.randint(1,10))

main()

# Calling Functions from an F String (section)
print(f'The number is {random.randint(1,100)}.')
print(f'{random.randint(0,1000):^10d}')

# This program the rolling of dice.
import random

MIN = 1
MAX = 6

def main():
    again = 'y'
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are:')
        print(random.randint(MIN,MAX)) 
        print(random.randint(MIN,MAX)) 
        again = input('Roll them again? (y = yes): ')

main()

x = random.randint(1,10) * 2

# This program display 10 tosses of a coin.
import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

main()

# The randrange, random, and uniform Functions (section)
number = random.randrange(10)
number = random.randrange(5,10)
number = random.randrange(0,101,10)

number = random.random()

number = random.uniform(1.0, 10.0)

# Random Number Seeds (section)
random.seed(10)

random.randint(1,100)
random.randint(1,100)
random.randint(1,100)
random.randint(1,100)
