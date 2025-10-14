""" Copying Lists """

list1 = [1,2,3,4]
list2 = list1
print(list1)
print(list2)

list1[0] = 99
print(list1)
print(list2)

# With Loop
list1 = [1,2,3,4]
list2 = []
for item in list1:
    list2.append(item)

# Alternative
list1 = [1,2,3,4]
list2 = [] + list1
print(list2)