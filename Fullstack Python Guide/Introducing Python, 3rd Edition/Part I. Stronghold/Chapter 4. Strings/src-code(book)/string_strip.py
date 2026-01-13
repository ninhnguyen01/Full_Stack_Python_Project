# It’s common to strip leading or trailing “padding” characters from a string, especially spaces. 
# The strip() functions shown here assume that you want to get rid of whitespace characters (' ', '\t', '\n') 
# if you don’t give them an argument. 
# The strip() function strips both ends, lstrip() only from the left, and rstrip() only from the right. 
# Let’s say the string variable world contains the string earth floating in spaces:

world = "    earth   "
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())

blurt = "What the...!!?"
print(blurt.strip('.?!'))

import string
string.whitespace
' \t\n\r\x0b\x0c'
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

blurt = "What the...!!?"
print(blurt.strip(string.punctuation))

prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))
