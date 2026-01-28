# Assign the string This is a test of the emergency text system to the variable test1, and write test1 to a file called test.txt.
test1 = 'This is a test of the emergency text system '
with open('test.txt', 'w') as f:
    f.write(test1)
    f.close()
