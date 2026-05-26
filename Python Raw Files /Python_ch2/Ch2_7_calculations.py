# Performing Calculations (Title)

# Reading

12 + 2

# hour * pay_rate
# Assign a value to the salary variable.
salary = 2500.0

# Assign a value to the bonus variable.
bonus = 1200.0

# Calculate the total pay by adding salary and bonus. Assign the result 
# to pay.
pay = salary + bonus

# Display the pay.
print('Your pay is', pay)

original_price = float(input("Enter the item's original price: "))
discount = original_price * 0.2

sales_price = original_price - discount
print('The sales price is', sales_price)

# Floating-Point and Integer Division (section)
5 / 2
5 // 2

-5 // 2

# Grouping with Parentheses (section)
a = 10
b = 2
result = (a + b) / 4

test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))

average = (test1 + test2 + test3) / 3.0
print('The average score is', average)

# The Exponent Operator (section)
# area = length ** 2
4**2
5**3
2**10

# The Remainder Operator (section)
# remainder operator or modulus operator %
total_seconds = float(input('Enter number of seconds: '))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60

print('Here is the the time in hours, minute, and seconds')
print('Hours: ', hours)
print('Minute: ', minutes)
print('Second: ', seconds)

# Converting Math Formulas to Programming Statements (section)
future_value = float(input("Enter the desired future value: "))
rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the money willl grow: '))
present_value = future_value / (1.0 + rate)**years
print = ('You will need to deposit this amount', present_value)

# Mixed-Type Expressions and Data Type Conversion (section)
my_number = 5 * 2.0
fvalue = 2.6
ivalue = int(future_value)

fvalue = -2.9
ivalue = int(fvalue)

ivalue = 2
fvalue = float(ivalue)

# Breaking Long Statements into Mutiple Lines (section)

# result = var1 * 2 + var2 * 3 + \
# var3 * 4 + var4 * 5 

# print("Monday's sales are", monday,
#       "Tuesday's sales are", tuesdsay,
#       "Wednesday's sales are", wednesday)

# total = (value1 + value2 +
#          value3 + value4 +
#          value5 + value6 )
