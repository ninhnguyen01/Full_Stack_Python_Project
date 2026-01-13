# You might also need \' or \" to specify a literal single or double quote 
# inside a string that’s quoted by the same character:

testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony)

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)

# And if you need a literal backslash, type two of them (the first escapes the second):
speech = 'The backslash (\\) bends over backwards to please you.'
print(speech)

# a raw string negates these escapes:
info = r'Type a \n to get a new line in a normal string'
print(info)
