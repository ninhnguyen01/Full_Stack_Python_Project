# You can use the built-in split() function to break a string into a list of smaller strings based on a separator. 
# Again, we look at lists in Chapter 8. 
# A list is a sequence of values, separated by commas and surrounded by square brackets:

tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))

# In the preceding example, the string is called tasks, and the string function is called split(), 
# with the single separator argument ,. 
# If you don’t specify a separator, split() uses any sequence of whitespace characters—newlines, spaces, and tabs:
print(tasks.split())
