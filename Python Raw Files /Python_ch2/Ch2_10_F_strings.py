# Displaying Formatted Output with F-strings (Title)

# Reading

print(f'Hello world')

name = 'Johnny'
print(f'Hello {name}.')

temperature = 45
print(f'It is currently {temperature} degrees.')

# Placeholder Expressions (section)
print(f'The value is {10 + 2}.')

val = 10
print(f'The value is {val + 2}.')

# Rounding Floating-Point Numbers (section)
# This program demonstrates how a floating-point 
# number can be rounded.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is: {monthly_payment:.2f}.')

# Round a number 3 decimal places:
pi = 3.1415926535
print(f'{pi:.3f}')

# Round value of a placeholder expression to 1 decimal point
a = 2
b = 3
print(f'{a / b:.1f}')

# Inserting Comma Separators (section)
# Comma Separators and Combo 
number = 1234567890.12345
print(f'{number:,}')

number = 1234567890.12345
print('f{number:,.2f}')

# This program demonstrates how a floating-point 
# number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay:,.2f}')

# Formatting a Floating Point Number as a Percentage (section)
# '%' Symbol to format a floating point as a percentage
discount = 0.5
print('f{discount:%}')

discount = 0.54
print('f{discount:.0%}')

# Formatting in Scientific Notation (section)
# Scientific Notation 
number = 12345.6789
print(f'{number:e}')
print(f'{number:.2e}')

# Formatting Integers (section)
number = 123456
print(f'{number:d}')

number = 123456
print(f'{number:,d}')

# Specifiying a Minimum Field Width (section)
number = 99
print(f'The number is {number:10}')

number = 12345.6789
print(f'The number is {number:12,.2f}')

# Comma Separator not in use (section)
number = 12345.6789
print(f'The number is {number:12.2f}')

# This program displays the following numbers
# in two columns. 
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Each number is displayed in a field of 10 spaces
# and rounded to 2 decimal places.
print(f'{num1:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')

# Aligning Values (section)
number = 22
print(f'The number is {number:10}')

name = 'Jay'
print(f'Hello {name:10}. Nice to meet you.')

# This program demonstrates how to center-align strings.
name1 = 'Gordon'
name2 = 'Smith'
name3 = 'Washington'
name4 = 'Alvarado'
name5 = 'Livingston'
name6 = 'Jones'

# Display the names. (section)
print(f'***{name1:^20}***')
print(f'***{name2:^20}***')
print(f'***{name3:^20}***')
print(f'***{name4:^20}***')
print(f'***{name4:^20}***')
print(f'***{name5:^20}***')
print(f'***{name6:^20}***')



# Concatenation with F-strings
name = 'Abbie Llyod'
department = 'Sales'
position = 'Manager'
print(f'Employee Name: {name} ' +
      f'Department Position: {department} ' +
      f'Postion: {position}')

# Implicit Concatenation with f-strings
print(f'Name: {name} '
      f'Department: {department} '
      f'Position: {position}')
