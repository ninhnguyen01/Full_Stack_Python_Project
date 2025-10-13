# Exceptions

# ZeroDivisionError:
# # This program divides a number by another number.
def num_divide():
 # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

 # Divide num1 by num2 and display the result.
    result = num1 / num2
    print(f'{num1} divided by {num2} is {result}')

num_divide() 

# ZeroDivisionError avoided with if statement:
# This program divides a number by another number.
def num_divide_control():
    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # If num2 is not 0, divide num1 by num2
    # and display the result.
    if num2 != 0:
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    else:
        print('Cannot divide by zero.')

    
num_divide_control()

# ValueError:
# This program calculates gross pay.
def gross_pay():
    # Get the number of hours worked.
    hours = int(input('How many hours did you work? '))

    # Get the hourly pay rate.
    pay_rate = float(input('Enter your hourly pay rate: '))

    # Calculate the gross pay.
    gross_pay = hours * pay_rate

    # Display the gross pay.
    print(f'Gross pay: ${gross_pay:,.2f}')

gross_pay()

# Exception handler:
# General Format:
# try:
#       statement
#       statement
#       etc.
# except ExceptionName:
#       statement
#       statement
#       etc.

# ValueError avoided with try/except:
# This program calculates gross pay.
def gross_pay_control():
    try:
        # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

        # Calculate the gross pay.
        gross_pay = hours * pay_rate

        # Display the gross pay.
        print(f'Gross pay: ${gross_pay:,.2f}')
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate must')
        print('be valid numbers.')

gross_pay_control()

# IOError avoided with try/except:
# This program displays the contents
# of a file.
def display_file():
    # Get the name of a file.
    filename = input('Enter a filename: ')
    text_folder = 'ch6_file/text/number.txt'
    try:
        # Open the file.
        if filename:
            infile = open(text_folder, 'r')
        # Read the file's contents.
            contents = infile.read()
        # Display the file's contents.
            print(contents)
        # Close the file.
            infile.close()
        
    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)

display_file()

# Mutilple Exceptions:
# This program displays the total of the
# amounts in the sales_data.txt file.
def multiply():
    # Initialize an accumulator.
    total = 0.0
    try:
    # Open the sales_data.txt file.
        infile = open('ch6_file/text/sales_data.txt', 'r')

    # Read the values from the file and
    # accumulate them.
        for line in infile:
            amount = float(line)
            total += amount

    # Close the file.
        infile.close()

    # Print the total.
        print(f'{total:,.2f}')

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occurred.')

multiply()

# One Except Clause to catch all Exceptions:
# This program displays the total of the
# amounts in the sales_data.txt file.
def add():
    # Initialize an accumulator.
    total = 0.0

    try:
    # Open the sales_data.txt file.
        infile = open('ch6_file/text/sales_data.txt', 'r')

    # Read the values from the file and
    # accumulate them.
        for line in infile:
            amount = float(line)
            total += amount

    # Close the file.
        infile.close()

    # Print the total.
        print(f'{total:,.2f}')
    except:
        print('An error occurred.')


add()

# Exception Default Error Message:
# This program calculates gross pay.
def calculate():
    try:
    # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))
    # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

    # Calculate the gross pay.
        gross_pay = hours * pay_rate

    # Display the gross pay.
        print(f'Gross pay: ${gross_pay:,.2f}')

    except ValueError as err:
        print(err)

calculate()

# This program displays the total of the
# amounts in the sales_data.txt file.
def display_total():
    # Initialize an accumulator.
    total = 0.0
    try:
    # Open the sales_data.txt file.
        infile = open('ch6_file/text/sales_data.txt', 'r')

    # Read the values from the file and
    # accumulate them.
        for line in infile:
            amount = float(line)
            total += amount

    # Close the file.
        infile.close()

    # Print the total.
        print(f'{total:,.2f}')
        
    except Exception as err:
            print(err)

display_total()

# The else Clause:
# General Format:
# try:
#       statement
#       statement
#       etc.
# except ExceptionName:
#       statement
#       statement
#       etc.
# else:
#       statement
#       statement
#       etc.

# This program displays the total of the
# amounts in the sales_data.txt file.
def accum():
    # Initialize an accumulator.
    total = 0.0

    try:
    # Open the sales_data.txt file.
        infile = open('ch6_file/text/sales_data.txt', 'r')
    # Read the values from the file and
    # accumulate them.
        for line in infile:
            amount = float(line)
            total += amount
    # Close the file.
        infile.close()

    except Exception as err:
        print(err)
    
    else:
    # Print the total.
        print(f'{total:,.2f}')

accum()

# finally Clause:
# General Format:
# try:
#       statement
#       statement
#       etc.
# except ExceptionName:
#       statement
#       statement
#       etc.
# finally:
#       statement
#       statement
#       etc.
