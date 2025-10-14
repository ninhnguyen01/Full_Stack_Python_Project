# List Comprehensions

# list comprehension
list1 = [1,2,3,4]
list2 = [item for item in list1]
print(list2)

# General Format Simple List Comprehension
# [result_expression iteration_expression]

# Square of all numbers in a first list
list1 = [1,2,3,4]
list2 = []

for item in list1:
    list2.append(item**2)
    print(list2)

# List comprehension
list1 = [1,2,3,4]
list2 = [item**2 for item in list1]
print(list2)

# List of strings and length in first list
str_list = ['Winken', 'Blinken', 'Nod']
len_list = []
for s in str_list:
    len_list.append(len(s))
    print(len_list)

# List comprehension
str_list = ['Winken', 'Blinken', 'Nod']
len_list = [len(s) for s in str_list]
print(len_list)

""" Using if Clauses with List Comprehension """
list1 = [1,12,2,20,3,15,4]
list2 = []

for n in list1:
    if n < 10:
        list2.append(n)
        print(list2)

# General Format if Clause to a List Comprehension:
# [result_expression iteration_expression if_clause]
list1 = [1,12,2,20,3,15,4]
list2 = [item for item in list1 if item < 10]
print(list2)

last_name = ['Jackson', 'Smith', 'Hildebrandt', 'Jones']
short_names = [name for name in last_name if len(name) < 6]
print(short_names)