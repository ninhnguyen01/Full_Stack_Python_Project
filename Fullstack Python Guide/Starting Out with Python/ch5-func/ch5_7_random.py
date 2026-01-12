# Introduction to Value-Returning Functions: Generating Random
# Numbers (Title)

# 5.22 What is a library function?
""" A prewritten function that performs some commonly needed task. """

# 5.23 Why are library functions like "black boxes"?
""" You can't see the operations being performed. """

# Import Statement Example
import math
# Generating Random Numbers 
import random
# 5.29 When the random module is imported, what does it use as
# a seed value for random number generation?
""" It uses the system time, retrieved from the computer's internal
# clock. """

# randit function
number = random.randint (1,100)

# This program displays a random number in the range 1 through 10
def main():
    number = random.randint(1,10)
    print(f'The number is {number}.')

main()


def main2():
    for count in range (5):
        number = random.randint(1,10)
        print(number)

main2()

print(random.randint(1,10))


def main3():
    for count in range (5):
        print(random.randint(1,10))

main3()

# Calling Functions from an F String (section)
print(f'The number is {random.randint(1,100)}.')
print(f'{random.randint(0,1000):^10d}')

# This program the rolling of dice.
MIN = 1
MAX = 6

def main4():
    again = 'y'
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are:')
        print(random.randint(MIN,MAX)) 
        print(random.randint(MIN,MAX)) 
        again = input('Roll them again? (y = yes): ')

main4()

x = random.randint(1,10) * 2

# This program display 10 tosses of a coin.
HEADS = 1
TAILS = 2
TOSSES = 10

def main5():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

main5()

# The randrange, random, and uniform Functions 
number = random.randrange(10)
number = random.randrange(5,10)
number = random.randrange(0,101,10)

number = random.random()

number = random.uniform(1.0, 10.0)

# Random Number Seeds 
# 5.30 What happens if the same seed value is always used for 
# generating random numbers? 
""" The random number functions would always generate the same series
of pseudorandom numbers. """

random.seed(10)

random.randint(1,100)
random.randint(1,100)
random.randint(1,100)
random.randint(1,100)
