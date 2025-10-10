#  Performing Calculations 

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

#  Floating-Point and Integer Division 
5 / 2
5 // 2

-5 // 2

# Operator Precedence 

# Order of Precedence 
# 1. Exponentiation **
# 2. Multiplication, division, and remainder * / // %   
# 3. Addition and Subtraction + -
# Note: There are exceptions.

# Grouping with Parentheses 
a = 10
b = 2
result = (a + b) / 4

test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))
average = (test1 + test2 + test3) / 3.0
print('The average score is', average)

#  The Exponent Operator 
# area = length ** 2
4**2
5**3
2**10

#  The Remainder Operator 
# remainder operator or modulus operator %
total_seconds = float(input('Enter number of seconds: '))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60
print('Here is the the time in hours, minute, and seconds')
print('Hours: ', hours)
print('Minute: ', minutes)
print('Second: ', seconds)

#  Converting Math Formulas to Programming Statements 
future_value = float(input("Enter the desired future value: "))
rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the money willl grow: '))
present_value = future_value / (1.0 + rate)**years
print('You will need to deposit this amount', str(present_value))

#  Mixed-Type Expressions and Data Type Conversion 
my_number = 5 * 2.0
fvalue = 2.6
ivalue = int(future_value)

fvalue = -2.9
ivalue = int(fvalue)

ivalue = 2
fvalue = float(ivalue)

#  Breaking Long Statements into Mutiple Lines
var1 = 1
var2 = 2
var3 = 3
var4 = 4

result = var1 * 2 + var2 * 3 + \
    var3 * 4 + var4 * 5 
print(result)

monday = 1000
tuesday = 1200
wedesday = 2500

print("Monday's sales are", str(monday),
      "\n",
       "Tuesday's sales are", str(tuesday),
       "\n",
       "Wednesday's sales are", str(wedesday))

value1 = 1
value2 = 2
value3 = 3
value4 = 4
value5 = 5
value6 = 6

total = (value1 + value2 +
          value3 + value4 +
          value5 + value6 )

print(total)
