primes = [2, 3, 5, 7, 11]
print(primes)
empty_list = []

# Adding Lists Together
items = ['cake', 'cookie', 'bread']

total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread','biscuit', 'tart']

# Python Lists: Data Types
numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]

# List Method .append()
orders = ['daisies', 'periwinkle']

orders.append('tulips')
print(orders)
# Result: ['daisies', 'periwinkle','tulips']

# List Indices
berries = ["blueberry", "cranberry",
"raspberry"]

print(berries[0])
print(berries[2])

# Negative List Indices
soups = ['minestrone', 'lentil', 'pho',
'laksa']

print(soups[-1])
print(soups[-3:])  # 'lentil', 'pho', 'laksa'
print(soups[:-2])  # 'minestrone', 'lentil'


# Modifying 2D Lists
berries[0]
berries[2]
# "blueberry"
# "raspberry"
soups = ['minestrone', 'lentil', 'pho',
'laksa']
soups[-1]
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'

# A 2D list of names and hobbies
class_name_hobbies = [["Jenny",
"Breakdancing"], ["Alexus",
"Photography"], ["Grace", "Soccer"]]

# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist.
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
# Output
# [["Jenny", "Meditation"], ["Alexus","Photography"], ["Grace", "Soccer"]]

# Accessing 2D Lists
# 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70],
["Sam", 67]]

# Access the sublist at index 0, and then access the 1st index of that sublist.
noelles_height = heights[0][1]
print(noelles_height)
# Output # 61

# List Method .remove()
# Create a list
shopping_line = ["Cole", "Kip", "Chris",
"Sylvana", "Chris"]

# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)
# Output
# ["Cole", "Kip", "Sylvana", "Chris"]

# List Method .count()
backpack = ['pencil', 'pen', 'notebook',
'textbook', 'pen', 'highlighter', 'pen']

numPen = backpack.count('pen')
print(numPen)
# Output: 3

# Determining List Length with len()
knapsack = [2, 4, 3, 7, 10]

size = len(knapsack)
print(size)
# Output: 5

# List Method .sort()
exampleList = [4, 2, 1, 3]

exampleList.sort()
print(exampleList)
# Output: [1, 2, 3, 4]

# List Slicing
tools = ['pen', 'hammer', 'lever']

tools_slice = tools[1:3] # ['hammer','lever']
tools_slice[0] = 'nail'

# Original list is unaltered:
print(tools) # ['pen', 'hammer', 'lever']

# sorted() Function
unsortedList = [4, 2, 1, 3]

sortedList = sorted(unsortedList)
print(sortedList)
# Output: [1, 2, 3, 4]

# List Method .insert()
# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim",
              "Isabella"]

# Here is how to insert "Vikor" after"Maxium" and before "Martim"
store_line.insert(2, "Vikor")
print(store_line)

# Output: ['Karla', 'Maxium', 'Vikor','Martim', 'Isabella']

# List Method .pop()
cs_topics = ["Python", "Data Structures",
"Balloon Making", "Algorithms", "Clowns101"]

# Pop the last element
removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)

# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'

# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)
# Output:
# ['Python', 'Data Structures','Algorithms']
