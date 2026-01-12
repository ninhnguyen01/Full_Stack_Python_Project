# Assume 'list1' is a list of integers. Write a statement
# that uses a list comprehension to create a second list
# containing the elements of 'list1' that are even numbers.
list1 = [60, 90, 100, 112, 212, 223]
list2 = [item for item in list1 if item % 2 == 0]
print(list2)
 