# Assume 'list1' is a list of integers. Write a statement
# that uses a list comprehension to create a second list
# containing the squares of the elements of 'list1'.
list1 = [2, 3, 4, 5, 6]
list2 = [item**2 for item in list1]
print(list2)