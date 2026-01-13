# Name Variables
# Python variable names have rules:
# They can contain these characters:

# Lowercase letters (a through z)
# Uppercase letters (A through Z)
# Digits (0 through 9)
# Underscore (_)
# They are case-sensitive: thing, Thing, and THING are different names.
# They must begin with a letter or an underscore, not a digit.
# They cannot be one of Python’s reserved words (also known as keywords).

# Find reserved words - better format
print(help("keywords"))

# Alternate
import keyword
print(keyword.kwlist)

validity = """
These are valid names:

a

a1

a_b_c___95

_abc

_1a

These names, however, are not valid:

1

1a

1_

name!

another-name
"""

print(validity)
