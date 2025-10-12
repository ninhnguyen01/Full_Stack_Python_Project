# The if-else Statement

""" General format of if-else statement """

# if condition:
#       statement
#       statement
#       etc.
# else:
#     statement
#     statement
#     etc.

# Example
temperature = 80
if temperature < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having.")

# Indentation in the if-else Statement

""" Guidlines for indentation: """
# if clause and the else clause are aligned.
# Both clause are each followed by a block of statements. 
# Statements in the block are consistently indented.

# Named constants to represent the base hours and the overtime 
# multiplier.
BASE_HOURS = 40 # Base hours per week
OT_MULTIPLER = 1.5 # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked. 
    overtime_hours = hours - BASE_HOURS
    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLER
    # Calulate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

    # Display the gross pay.
    print(f'The gross pay is ${gross_pay:,.2f}. ')
