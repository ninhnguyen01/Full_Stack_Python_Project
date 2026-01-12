# Write a loop that counts the number of digits that
# appear in the string referenced by 'mystring'.

mystring = '12345'
digit = 0
for d in mystring:
    if mystring.isdigit():
        digit += 1
        print(digit)
