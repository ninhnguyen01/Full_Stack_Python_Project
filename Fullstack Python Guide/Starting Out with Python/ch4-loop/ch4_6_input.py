# Input Validation Loops (Title)

# 4.20 What does the phrase "garbage in,garbage out (GIGO)" mean?
""" It refers to the fact that computers cannot tell the difference
# between good and bad data (i.e., bad data input = bad data output) """

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
# 4.21 Give a general prescription of the input validation process.
""" If the input is invalid, the program should discard it and
# prompt the user to enter the correct data. """
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
    another = input('Do you have another item ' + 
    '(Enter [y] for yes)?: ')

# Revised program 
# This program calculates retail prices.
MARK_UP = 2.5
another = 'y'       # variable to control loop
# Process one or more items.
while another == 'y' or another == 'Y':
    # --- Get the items's wholesale cost. ---
    # -> What is a prime reading? What is its purpose?
    """A prime reading is an input operation that get the first input
    value that will be tested before an input validation loop. """
    # -> If the input that is read by the priming read is valid,
    # how many times will the input validation loop iterate?
    """ 0 """
    wholesale = float(input("Enter the item's wholesale cost: "))
    # -- Validate the wholesale cost. --
    # Describe the steps that are generally taken when an input
    # validation loop is used to validate data. 
    """ Input is read, pretest loop is executed. Input data invalid,
    body of loop executes. In body of loop, error message display
    for user. Input read again. Loop repeat if input is invalid. """
    while wholesale < 0:
        print('ERROR: The cost cannot be negative.')
        wholesale = float(input('Enter the correct ' +
        'wholesale cost: '))
    # Calculate the retail price.
    retail = wholesale * MARK_UP
    # Display the retail price.
    print(f'Retail price: ${retail:,.2f}')
    # Do this again?
    another = input('Do you have another item ' + 
    '(Enter [y] for yes)?: ')
