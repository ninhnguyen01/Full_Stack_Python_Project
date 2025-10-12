# Comparing Strings 

# Reading

name1 = 'Marie'
name2 = 'Mark'
if name1 == name2:
    print('The names are the same.')
else:
    print('The names are NOT the same.')

# This program compare two strings.
# Get a password from the user.
password = input('Enter the password: ')

# Determine whether the correct password was entered.
if password == 'prospero':
    print('Password accepted: ')
else:
    print('Sorry, that is the wrong password.')

# WARNING
# String comparisons are case sensitive.

# This program compare strings with the '<' operator.
# Get two names fron the user.
name1 = input('Enter a name (last name): ')
name2 =  input ('Enter another name (first name) ')

# Display the names in Alphabetical order.
print('Here are the names, listed alphabetically.')

if name1 > name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
