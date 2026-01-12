# The math Module (Title)

# The math.pi and math.e Values
""" area = math.pi * radius**2 """

# 5.34 What import statement do you need to write in a program that
# uses the math module?
""" import math """

# sqrt function demo
import math

def main():
    number = float(input('Enter a number: '))
    square_root = math.sqrt(number)
    print(f'The square root of {number} is {square_root}.')

main()

# This program calculates the length of a right triangle's
# hypotenuse. 
def main2():
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))
    c = math.hypot(a, b)

    print(f'The length of the hypotenuse is {c}.')

main2()
