# Nested Decision Structures and the if-else-if Statement

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
if salary > MIN_SALARY:
    if years_on_job > MIN_YEARS:
        print('You qualify for a loan.')
    else:
        print(f'You must have been employed ' 
    f' for at least {MIN_YEARS} '
    f' years to qualify.')
else: 
    print(f'You must earn at least $'
    f' {MIN_SALARY:,.2f}  '
    f' per year to qualify. ')

""" Testing a series of condition """
# Multiple Nested Decision Structures.

# This program gets a numeric test score from the user and displays the
# corresponding letter grade.

# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user
score = int(input('Enter your test score: '))

# Determine the grade.
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

""" The if-elif-else statement """

# if condition_1:
#   statement
#   statement
#   etc.

# elif condition_2:
#   statement
#   statement
#   etc.

# Insert as many elif clauses as necessary...

# else:
#       statement
#       statement
#       etc.

if score >= A_SCORE:
    print('Your grade is A.')
elif score >= B_SCORE:
    print('Your grade is B.')
elif score >= C_SCORE:
    print('Your grade is C.')
elif score >= D_SCORE:
    print('Your grade is D.')
else:
    print('Your grade is F.')
