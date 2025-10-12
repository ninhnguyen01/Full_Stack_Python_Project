# Introduction to Value-Returning Functions: Generating Random Numbers

# Import Statement Example
# import math

""" Generating Random Numbers """
import random

# This program displays a random number in the range 1 through 10
def main():
    count = []
    for number in range(5):
        number = random.randint (1,100)
        count.append(number)
        print(count)

main()


""" Calling Functions from an F String """
print(f'The number is {random.randint(1,100)}.')
print(f'{random.randint(0,1000):^10d}')

# This program the rolling of dice.
MIN = 1
MAX = 6

def dice():
    again = 'y'
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are:')
        print(random.randint(MIN,MAX)) 
        print(random.randint(MIN,MAX)) 
        again = input('Roll them again? (y = yes): ')

dice()

# This program display 10 tosses of a coin.
HEADS = 1
TAILS = 2
TOSSES = 10

def coin_toss():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

coin_toss()
