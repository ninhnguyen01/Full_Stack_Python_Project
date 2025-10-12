# Input Validation Loops

# Get a test score.
score = int(input('Enter a test score: '))

# Make sure it is not less than 0
while score < 0:
    print('ERROR: The score cannot be negative.')
    score = int(input('Enter the correct score: '))

# Input validation loop is sometimes called 'error trap' or 
# an 'error handler'.

# Get a test score.
score = int(input('Enter a test score: '))

# Make sure it is not less than 0 or greater than 100.
while score < 0 or score > 100:
    print('ERROR: The score cannot be negative')
    print('or greater than 100.')
    score = int(input('Enter the correct score: '))

# This program calculates retail prices.
MARK_UP = 2.5
another = 'y'       # variable to control loop

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the items's wholesale cost.
    wholesale = float(input("Enter the item's wholesale cost: "))
    # Calculate the retail price.
    retail = wholesale * MARK_UP
    # Display the retail price.
    print(f'Retail price: ${retail:,.2f}')
    # Do this again?
    another = input('Do you have another item? ' + 
    '(Enter y for yes): ')

# Revised program (below)
# This program calculates retail prices.
MARK_UP = 2.5
another = 'y'       # variable to control loop

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the items's wholesale cost.
    wholesale = float(input("Enter the item's wholesale cost: "))
    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: The cost cannot be negative.')
        wholesale = float(input('Enter the correct ' +
        'wholesale cost: '))
    # Calculate the retail price.
    retail = wholesale * MARK_UP
    # Display the retail price.
    print(f'Retail price: ${retail:,.2f}')
    # Do this again?
    another = input('Do you have another item? ' + 
    '(Enter y for yes): ')

""" --- Note ----

- What does the phrase "garbage in, garbage out (GIGO)" mean?
It refers to the fact that computers cannot tell the difference
between good and bad data (i.e., bad data input = bad data output)
 
"""