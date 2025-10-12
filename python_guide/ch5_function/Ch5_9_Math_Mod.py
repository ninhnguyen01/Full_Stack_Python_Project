# The math Module

""" This program demonstrates the sqrt function. """
import math

def main():
    number = float(input('Enter a number: '))
    square_root = math.sqrt(number)
    print(f'The square root of {number} is {square_root}.')

main()

""" This program calculates the length of a right triangle's hypotenuse. """
def main2():
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))
    c = math.hypot(a, b)

    print(f'The length of the hypotenuse is {c}.')

main2()
