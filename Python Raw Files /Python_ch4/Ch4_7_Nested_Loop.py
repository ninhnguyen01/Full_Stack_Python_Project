# Nested Loops (Title)

# Reading

for seconds in range (60):
    print(seconds)

for minutes in range (60):
    for seconds in range (60):
        print(minutes, ':', seconds)

for hours in range (24):
    for minutes in range (60):
        for seconds in range (60):
            print(hours, ':', minutes, ':', seconds)

# This program averages test scores. It asks the user for 
# the number of students and the number of test scores per
# student.
# Get the number of students.
num_students = int(input('How many students do you have? '))
# Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student? '))
# Determine each student's average test score.
for student in range (num_students):
    # Intialize an accumulator for the test scores.
    total = 0.0
    # Display the student number.
    print(f'Student number {student + 1}')
    print('-----------------')
    # Get the student's test scores.
    for test_num in range (num_test_scores):
        print(f'Test number {test_num + 1}', end = '')
        score = float(input(': '))
        # Add the score to the accumulator.
        total += score 
    # Calculate the average test score for this student.
    average = total / num_test_scores 
    # Display the average.
    print(f'The average for student number {student + 1} ' 
    f'is: {average:.1f}')
    print()

# Using Nested Loops to Print Patterns (Spotlight) 
for col in range (6):
    print('*', end = '')
    
for row in range (8):
    for col in range (6):
        print('*', end = '')
    print()

# This program displays a rectangular pattern of asterisks.
rows = int(input('How many rows? '))
cols = int(input('How many columns? '))

for r in range (rows):
    for c in range (cols):
        print('*', end = '')
    print()

# This program displays a triangle pattern.
BASE_SIZE = 8
for r in range (BASE_SIZE):
    for c in range (r + 1):
        print('*', end = '')
    print()

# This program displays a stair-step pattern.
NUM_STEPS = 6
for r in range (NUM_STEPS):
    for c in range (r):
        print(' ', end = '')
    print('#')

