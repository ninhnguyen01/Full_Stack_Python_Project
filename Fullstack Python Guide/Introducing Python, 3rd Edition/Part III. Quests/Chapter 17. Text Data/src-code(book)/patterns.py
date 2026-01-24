import string
import re
printable = string.printable
print(len(printable))
print(printable[0:])
print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))

# The characters ^ and $ are called anchors: ^ anchors the search to the beginning of the search string, and $ anchors it to the end. 
# The .$ characters match any character at the end of the line, including a period, so that works. 
# To be more precise, we should escape the dot to match it literally
