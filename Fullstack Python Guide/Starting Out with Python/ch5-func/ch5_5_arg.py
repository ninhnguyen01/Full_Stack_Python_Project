# Passing Arguments to Functions (Title)

# This Program demonstrates an argument being passed to a function.
def main():
    value = 5
    show_double(value)

# The show_double function accepts an argument and displays double
# its value.
def show_double(number):
    result = number * 2
    print(result)

main()

show_double(50)

# Parameter Variable Scope 
# This program converts cups to fluid ounces
def main2():
    intro()
    cups_needed = int(input('Enter the number of cups: '))
    cups_to_ounces(cups_needed)
def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    print()
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That converts to {ounces} ounces.')

main2()

# Passing Multiple Arguments 
# This program demonstrates a function that accepts two arguments.
def main3():
    print('The sum of 12 and 45 is')
    show_sum(12,45)
def show_sum(num1,num2):
    result = num1 + num2
    print(result)

main3()

# This program demonstrates passing two string arguments to a
# function.
# 5.13 What are the pieces of data that are passed into a function called?
""" Arguments. """
def main4():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name,last_name)

def reverse_name (first, last):
    print(last, first)

main4()

# Making Changes to Parameters 
def main5():
    value = 99
    print(f' The value is {value}.')
    change_me(value)
    print(f' Back in main the value is {value}.')

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print(f'Now the value is {arg}.')

main5()

# Keyword Arguments 
# parameter_name = value
# This Program demonstrates keyword arguments.
def main6():
    # 5.14 What are the variables that receive pieces of data in a 
    # function called?
    # A: Parameters.
    show_interest(rate=0.01, periods= 10, principal = 10000.0)
def show_interest (principal, rate, periods):
    interest = principal * rate * periods
    print(f'The simple interest will be ${interest:,.2f}.')

main6()

# This program demonstrates passing two strings as keyword 
# arguments to a function.
def main7():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(last=last_name, first=first_name)

def reverse_name (first, last):
    print(last, first)

main7()

# Mixing Keyword Arguments with Positional Arguments 
show_interest(10000.0, rate = 0.01, periods=10)

# 5.15 What is a parameter variable's scope?
""" The entire function in which the parameter is declared. """

# 5.16 When a parameter is changed, does this affect the argument
# that was passed into the parameter?
""" No, it does not. """
