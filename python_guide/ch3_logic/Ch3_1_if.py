# The if Statement

#  Sequence Structure Example [Execute in the order in which they appear] 
name = input('What is your name? ')
age = int(input('What is your age? '))
print('Here is the date you enter: ')
print('Name: ', name)
print('Age: ', age)

""" General format of if statement """
# if condition:
#       statement
#       statement
#       etc.

# Boolean Expressions and Relational Operators
# Example Below
x = 1
y = 0
x > y 
y > x

print(x > y)
print(y > x)

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
