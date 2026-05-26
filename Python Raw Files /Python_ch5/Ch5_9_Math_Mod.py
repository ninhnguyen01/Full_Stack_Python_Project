# The math Module (Title)

# Reading

# This program demonstrates the sqrt function. (section)
import math

def main():
    number = float(input('Enter a number: '))
    square_root = math.sqrt(number)
    print(f'The square root of {number} is {square_root}.')

main()

# This program calculates the length of a right triangle's
# hypotenuse. (section)
import math

def main():
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))
    c = math.hypot(a, b)

    print(f'The length of the hypotenuse is {c}.')

main()

# The math.pi and math.e Values

# area = math.pi * radius**2
