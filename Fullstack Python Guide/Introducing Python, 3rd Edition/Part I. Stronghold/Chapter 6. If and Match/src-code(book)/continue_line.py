# augmented assignment operator example: +=
sum = 0
sum += 1
sum += 2
sum += 3
sum += 4
print(sum)

# no syntax error with '\'
sum2 = 1 + \
    2 + \
    3 + \
    4
print(sum2)

# Here’s the preferred way to make multiline expressions: 
# Python doesn’t squawk about line endings if you’re in the middle of paired parentheses (or square brackets or curly braces):
sum = (
     1 +
     2 +     
     3 +
     4)

print(sum)
