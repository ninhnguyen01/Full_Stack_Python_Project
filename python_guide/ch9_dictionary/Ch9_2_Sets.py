# Sets

# set - an object that stores a collection of data
# all elements must be unique
# sets are unordered
# elements can be different data types.

""" Creating a Set """
# 1 argument (list,tuple,string)
myself = set()
myself = set(['a','b','c'])
myself = set('abc')
myself = set(['one','two','three'])

""" Getting the Number of Elements in a Set """
myset = set([1,2,3,4,5])
len(myset)

""" Adding and Removing Elements """
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# update method
myset = set([1,2,3])
myset.update([4,5,6])
print(myset)

set1 = set([1,2,3])
set2 = set([8,9,10])
set1.update(set2)
print(set1)
print(set2)

myset = set([1,2,3])
myset.update('abc')
print(myset)

# remove method (raise KeyError exception)
myset = set([1,2,3,4,5])
print(myset)
myset.remove(1)
print(myset)

# discard method (no exception)
myset.discard(5)
print(myset)
myset.discard(99)
# myset.remove(99)

# clear method 
myset = set([1,2,3,4,5])
print(myset)
myset.clear()
print(myset)

""" Using the 'for' Loop to Iterate over a Set """
# General Format:
#   for var in set:
#       statement
#       statement
#       etc.

myself = set(['a','b','c'])
for val in myset:
    print(val)

""" Using the 'in' and 'not in' Operators to Test for a Value in a Set """
myset = set([1,2,3])
if 1 in myset:
    print('The value 1 is in the set.')

myset = set([1,2,3])
if 99 not in myset:
    print('The value 99 is not in the set.')

""" Finding the Union of Sets """

# General Format:
# set1.union(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.union(set2)
print(set3)

# alternative
# General Format:
# set1 | set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 | set2
print(set3)

""" Finding the Intersection of Sets """

# General Format:
# set1.intersection(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.intersection(set2)
print(set3)

# alternative
# General Format:
# set1 & set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 & set2
print(set3)

""" Finding the Difference of Sets """

# General Format:
# set1.difference(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.difference(set2)
print(set3)

# alternative
# General Format:
# set1 - set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 - set2
print(set3)

""" Finding the Symmetric Difference of Sets """

# General Format:
# set1.symmetric_difference(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.symmetric_difference(set2)
print(set3)

# alternative
# General Format:
# set1 ^ set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 ^ set2
print(set3)

""" Finding Subsets and Supersets """
set1 = set([1,2,3,4])
set2 = set([2,3])
set2.issubset(set1)
set1.issuperset(set2)

# alternative
set1 = set([1,2,3,4])
set2 = set([2,3])
set2 <= set1
set1 >= set2
set1 <= set2

# This program demonstrates various set operations.
baseball = set(['Jodi','Carmen','Aida','Alicia'])
basketball = set(['Eva','Carmen','Alicia','Sarah'])
print('The following students are on the baseball team:')
for name in baseball:
    print(name)

print()
print('The following students are on the basketball team:')
for name in basketball:
    print(name)

print()
print('The following students play both baseball and basketball:')
for name in baseball.intersection(basketball):
    print(name)

print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

print()
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)

print()
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)

print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)

""" Set Comprehensions """
# an expression that reads a sequence of input elements to
# produce a set.

# List
set1 = set([1,2,3,4,5])
# Set
set2 = {item for item in set1}

# List
set1 = set([1,2,3,4,5])
# Set
set2 = {item**2 for item in set1}

# List
set1 = set([1,20,2,40,3,50])
# Set (if)
set2 = {item for item in set1 if item < 10}

