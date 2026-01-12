# The if Statement (Title)

# General format of if statement 
"""if condition:
       statement
       statement
       etc. """

# 3.1 What is a control structure?
""" A logical design that controls the order in which a set
of statements execute. """

# 3.2 What is a decision structure?
""" A program structure that can execute a set of statements only under
certain circumstances. """

# 3.3 What is a single alternative decision strcuture?
""" A decision structure that provides a single alternative path for
execution. """

# 3.4 What is a Boolean Expression?
""" An expression that can be evaluated as either true or false. """

# 3.5 What types of relationships between values can you test with
# relational operators?
""" Greater than (>), less than (<), greater than or equal to (>=),
less than or equal to (<=), equal to (==), not equal to (!=). """

# Sequence Structure Example [Execute in the order in which they appear] 
name = input('What is your name? ')
age = int(input('What is your age? '))
print('Here is the date you enter: ')
print('Name: ', name)
print('Age: ', age)

# Boolean Expressions and Relational Operators.
# Example Below
x = 1
y = 0
x > y 
y > x

# Putting It All together
# Example Decision Structure
sales = 5500.0
if sales > 5000.0:
    bonus = 500.0
    commission_rate = 0.12
    print('You met your sales quota!')

# This program gets three test scores and displays their average.
# It congratulates the user if the average is a high score.
# The HIGH_SCORE named constant holds the value that is considered a high
# score.
HIGH_SCORE = 95

# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score,
average = (test1 + test2 + test3) / 3

# Print the average.
print(f'The average score is {average}.')

# If the average is a high score, congratulate the user.

if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!') 
