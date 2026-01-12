# Write a loop that counts the number of lowercase
# characters that appear in the string referenced 
# by 'mystring'.

mystring = 'mystring'
lower = 0
for l in mystring:
    if mystring.islower():
        lower += 1
        print(lower)
        