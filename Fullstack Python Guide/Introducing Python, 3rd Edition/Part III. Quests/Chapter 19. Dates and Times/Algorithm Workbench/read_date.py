# Read the text file today.txt into the string today_string.
# Parse the date from today_string.
with open('Chapter 19. Dates and Times/Algorithm Workbench/today.txt','r') as f:
    today_string = f.read()
    print(today_string)
    f.close()
