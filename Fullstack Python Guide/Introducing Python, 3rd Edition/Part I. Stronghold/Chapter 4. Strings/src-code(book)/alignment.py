# Now, let’s work with some layout alignment functions. 
# The string is aligned within the specified total number of spaces (30 here).

setup = 'a duck goes into a bar...'

# Center the string within 30 spaces:
print(setup.center(30))

# Left-justify:
print(setup.ljust(30))

# Right-justify:
print(setup.rjust(30))
