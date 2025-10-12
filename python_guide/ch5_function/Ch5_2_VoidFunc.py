# Defining and calling a Void Function

# General Format of a Function Definiton:

# def function_name():
#     statement
#     statement
#     etc.

# This program demonstrates a function.
# First, defined a function named message.
def message():
    print('I am Arthur,')
    print('King of the Britons.')
# Call the message function
message()

# This program has two functions. 
# First we define the main function.
def main():
    print('I have a message for you.')
    message()
    print('Goodbye!')

# Next we define the message function.
def message():
    print('I am Arthur,')
    print('King of the Britons.')

# Call the main function.
main()
