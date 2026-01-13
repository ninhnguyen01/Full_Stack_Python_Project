# The old style of string formatting has the form format_string % data.
# %s String
# %d Decimal integer
# %x Hex integer
# %o Octal integer
# %f Decimal float
# %e Exponential float
# %g Decimal or exponential float
# # %% A literal %
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

print('%d%%' % 100)

# string and integer interpolation:
cat = 'Chester'
weight = 28
print("My cat %s weighs %s pounds" % (cat, weight))

# Let’s take a quick look at these values:

# An initial % character.
# An optional alignment character: nothing or + means right-align, and - means left-align.
# An optional minwidth field width to use.
# An optional . character to separate minwidth and maxchars.
# An optional maxchars (if conversion type is s) indicating the number of characters to print from the data value. 
# If the conversion type is f, this specifies precision (the number of digits to print after the decimal point).
# The conversion type character from the earlier table.

thing = 'woodchuck'

print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)

thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)

# New style: {} and format()
# “New style” formatting has the form format_string.format(data).
thing = 'woodchuck'
print('{}'.format(thing))

# The arguments to the format() function need to be in the same order as the {} placeholders in the format string:
thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))

# With new-style formatting, you can also specify the arguments by position like this:
print('The {1} is in the {0}.'.format(place, thing))

# The value 0 refers to the first argument, place, and 1 refers to thing.
# The arguments to format() can also be named arguments:
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))

# or a dictionary:
d = {'thing': 'duck', 'place': 'bathtub'}

# In the following example, {0} is the first argument to format() (the dictionary d):
print('The {0[thing]} is in the {0[place]}.'.format(d))

# These examples all print their arguments with default formats. 
# New-style formatting has a slightly different format string definition from the old-style one (examples follow):

#  An initial colon (:).
#  An optional fill character (the default is ' ') to pad the value string if it’s shorter than minwidth.
#  An optional alignment character. This time, left alignment is the default. The < character also means left, > means right, and ^ means center.
#  An optional sign for numbers. Nothing means prepend a minus sign (-) only for negative numbers. Using ' ' means prepend a minus sign for negative numbers, and a space (' ') for positive ones.
#  An optional minwidth.
#  An optional period (.) to separate minwidth and maxchars.
#  An optional maxchars.
#  The conversion type.

# The following shows various ways of formatting a string with two string variables:
thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The {:10s} is at the {:10s}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))


# Newest Style: f-strings
# F-strings appeared in Python 3.6 and are now the recommended way of formatting strings.
# To make an f-string, do the following:
# Type the letter f or F directly before the initial single- or triple-quote characters.
# Include variable names or expressions within curly braces ({}) to get their values interpolated into the string.
# This approach is like the previous section’s new-style formatting, 
# but without the format() function, and without empty brackets ({}) or positional ones ({1}) in the format string. 
# F-strings use curly braces ({}) differently:
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')

# As I already mentioned, expressions are also allowed inside the curly braces:
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')

# F-strings use the same formatting language (width, padding, alignment) as new-style formatting, after a colon (:):
print(f'The {thing:>20} is in the {place:.^20}')

# Starting in Python 3.8, f-strings gain a new shortcut that’s helpful when you want to print variable names as well as their values. 
# This is handy when debugging. The trick is to have a single = after the name in the {}-enclosed part of the f-string:

print(f'{thing =}, {place =}')

# The name can be an expression, and it will be printed literally:
print(f'{thing[-4:] =}, {place.title() =}')

# Finally, the = can be followed by a : and the formatting arguments like width and alignment:
print(f'{thing = :>4.4}')
