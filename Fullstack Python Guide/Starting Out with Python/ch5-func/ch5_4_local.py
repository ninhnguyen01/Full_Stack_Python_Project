# Local Variables (Title)

# 5.10 What is a local variable? How is access to a local variable
# restricted?
""" a local variable is a variable that is declared inside a function.
It belongs to the function in which it is declared, and only statements
in the same function can access it. """

# 5.11 What is a variable's scope?
""" The part of a program in which a variable may be accessed. """

# 5.12 Is it permissible for a local variable in one function to 
# have the same name as a local variable in a different function? 
""" Yes, it is permissible. """

# This program demonstrates two functions that have local variables
# with the same name.
def main():
    texas()
    california()
def texas():
    birds = 5000
    print(f'texas has {birds} birds.')
def california():
    birds = 8000
    print(f'california has {birds} birds.')

main()
