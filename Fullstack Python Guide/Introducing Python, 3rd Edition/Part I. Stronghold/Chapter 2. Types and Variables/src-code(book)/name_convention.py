# Follow Naming Conventions

# Python also has conventions when naming variables. They aren't rules, like those I just mentioned, 
# but they'll help you be consistent with other Python code out there:

name_convention = """Python variables should use snake case: lowercase letters (and possibly digits) separated by the underscore (_) character. 
Examples: x_squared, num_ghosts.

Other languages capitalize the first letter too: XSquared, NumGhosts. 
Python also likes this convention when you're defining object classes, which are coming in Chapter 11. 
Sometimes this is called Pascal case or upper camel case.

Although Python doesn't have true constants (variables whose value can't change), 
it recommends snake case with all caps to help everyone remember that this variable should not be modified after its initial assignment: 
MAX_ITEMS, SECRET_CODE.

Python really seems to like that humble underscore character:

A name that starts with a single underscore (_) is treated as sort of private by the import statement (see Chapter 12).

A name that starts with two underscores (__) is treated specially when creating object classes (see Chapter 11).

Names that start and end with double underscores are used for so-called magic, or dunder, methods in object classes (also in Chapter 11).
"""

print(name_convention)