# Logical Operators

""" The 'and' Operator """
# if temperature < 20 and minutes > 12:
    # print('The temperature is in the danger zone.')

""" The 'or' Operator """

# if temperature < 20 or temperature > 100:
    # print('The temperature is too extreme.')

# The 'not' Operator
# if not (temperature > 100):
    # print('This is below the maximum temperature.')

""" Compound expression with 'and' Operator """
# This program determines whether a bank customer qualifies for 
# a loan.
MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on a job

# Get the customer's annaul salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
'years employed: '))

# Determine whther the customer qualifies.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('You qualify for a loan.')
else:
    print('You do not qualify for a loan.')

""" Compound Expression with 'or' Operator """
# This program determines whether a bank customer qualifies for 
# a loan.
MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on a job

# Get the customer's annaul salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
'years employed: '))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('You qualify for a loan.')
else:
    print('You do not qualify for a loan.')

""" Checking Numeric Ranges with Logical Operators """
# if x >= 20 or x <= 40:
#     print('The value is in the acceptable range.')

# if x < 20 or x > 40:
#     print('The value is outside the acceptable range.')
