#  More About the print Function 

# Suppressing the Print Function's Ending Newline
print('one')
print('two')
print('three')

# To print space instead of newline character (new line of output)
print('one', end=' ')
print('two', end=' ')
print('three')

# To print nothing at the end of its output
print('one', end='')
print('two', end='')
print('three', end='')

# Specifiying an Item Separator (section)
print('One', 'Two', 'Three')

# Use sep='' if you want no space printed between items
print('One' , 'Two', 'Three', sep='')

# Special argument to separate multiple items (similar to above)
print('One', 'Two', 'Three', sep='*')

# Additional example
print('One', 'Two', 'Three', sep='~~~')

# Escape Characters 

# Escape Character \n
print('One/nTwo/nThree')

# Escape Character \t
print('Mon\tTues\tWed')
print('Thur\tFri\tSat')

# Escape Character \' and \" to display quotation marks
print("Your assignment is to read \"Hamlet\" by tomorrow.")
print('I\'m ready to being.') 

# Escape Character \\ to display a backslash
print('The path is C:\\temp\\data.')
