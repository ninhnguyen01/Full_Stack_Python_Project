#  Variables

# Variable = Expression
width = 10
length = 5
print(width)
print(length)
print('width') # output is a string
print(width) # output is the expression

# This example demonstrates a variable.
room = 503 
print('I am staying in room number')
print(room)

# Create two variables: top_speed and distance.
top_speed = 160
distance = 300
# Display the values referenced by the variables.
print('The top speed is') 
print(top_speed)
print('The distance traveled is')
print(distance)

#  Variable Naming Rules

# 1) Python keywords (DO NOT USE)
# 2) Variable name (NO SPACES ALLOW)
# 3) 1st character only a to z, A to Z, or underscore (_)
# 4) AFTER FIRST CHARACTER a to z, A to Z, 0 to 9, or underscore (_)
# 5) Uppercase and lowercase characters are distinct.

# Displaying Multiple Items with the 'print' Function
# This program demonstrates a variable.
room = 503
print('I am staying in room number', room)

#  Variable Reassignment 
# This program demonstrates program reassignment.
dollars = 2.75
print('I have', dollars, 'in my account.')
dollars = 99.95
print('But now I have', dollars, 'in my account!' )

# Numeric Data Types and Literals
type(1)
type(1.0)

# WARNING
# You can't write currency symbols, spaces or commas in numeric literals.
# Value = $4,567.99 <-- ERROR!

# Store Strings with the str Data type 
# creat variables to reference two strings.
first_name = 'Kathyrn'
last_name = 'Marino'
print(first_name, last_name)

# Reassigning a Variable to a Different Type 
x = 99
print(x)
x = 'Take me to your leader'
print(x)
