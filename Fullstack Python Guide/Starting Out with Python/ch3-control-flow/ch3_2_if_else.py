# The if-else Statement (Title)

# General format of if-else statement: 
""" if condition:
       statement
       statement
       etc.
       
    else:
     statement
     statement
     etc. """

# Indentation in the if-else Statement 
""" Guidelines for indentation:
if clause and the else clause are aligned.
Both clause are each followed by a block of statements. 
Statements in the block are consistently indented. """

# 3.8 How does a duel alternative decision structure work?
""" It has two possible paths of execution - one path is taken if a
condition is true, and the other path is taken if the condition is
false. """

# 3.9 What statement do you use in Python to write a duel alternative
# decision structure?
""" if-else statement """

# 3.10 When you write an if-else statement, under what circumstances do 
# the statements that appear after the else clause execute?
""" When the condition is false. """

# Example
temperature = 80
if temperature < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having.")

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
