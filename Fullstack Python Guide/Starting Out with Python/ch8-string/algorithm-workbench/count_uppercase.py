# Write code that makes a copy of a string with all 
# occurrences of the lowercase 't' converted to uppercase. 

word = 'Titan'
if 't' in word:
    copy = word.replace('t','T')
    print(copy)
