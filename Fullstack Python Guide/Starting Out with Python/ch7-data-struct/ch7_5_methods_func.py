# List Methods and Useful Built-in Functions

# list methods
# ------------
# append(item)
# index(item)
# insert(index,item)
# sort()
# remove(item)
# reverse()

# The 'append' Method 
# add items to a list

# The 'index' Method 
# to know if an item is in a list and to locate

# The 'insert' Method 
# insert an item at a specific position

# This program demonstrates how the append method can be used 
# to add items to a list

# The 'sort' Method 
# rearrange elements in a list (low to high)

# The 'remove' Method 
# remove an item from list

# The 'reverse' Method 
# reverse order of item in list

# The 'del' statement 
# delete element from a specific index

# 7.15 What is the difference between calling a list's 'remove'
# method and using the 'del' statement to remove an element? 
""" The remove method searches for and removes an element 
# containing a specific value. The del statement removes an element
# at a specific index. """

# 7.16 How do you find the lowest and highest values in a list?
""" You can use the built-in min and max functions. """

# 7.17 Assume the following statment appears in a program:
# names = []
# Which of the following statements would you use to add 
# the string 'Wendy' to the list at index 0? 
""" You would use names.append('Wendy').
This is because element 0 does not exist. """

# 7.18 Describe the following list methods:
# a. index - searches for an item in the list,
# and returns the index of the first element containing that
# item.
# b. insert - inserts an item into the list at
# a specified index.
# c. sort - sorts the items in the list to appear
# in ascending order.
# d. reverse - 
# d. The 'reverse' method reverses the order of the items
# in the list.

def main():
    name_list = []
    again = 'y'
    while again == 'y':
        name = input('Enter a name: ')
        name_list.append(name)
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()
    print('Here are the names you entered.')

    for name in name_list:
        print(name)

if __name__ == '__main__':
    main()

# This program demonstrates how to get the index of an item
# in a list and then replace that item with a new item.
def main2():
    food = ['Pizza', 'Burgers', 'Chips']
    print('Here are the items in the food list:')
    print(food)
    item = input('Which item should I change? ')
    try:
        item_index = food.index(item)
        new_item = input('Enter the new value: ')
        food[item_index] = new_item
        print('Here is the revised list:')
        print(food)
    except ValueError:
        print('That item was not found in the list.')

if __name__ == '__main__':
    main2()

# This program demonstrates the 'insert' method.
def main3():
    names = ['James','Kathryn','Bill']
    print('The list before the insert:')
    print(names)

    names.insert(0,'Joe')
    print('The list after the insert:')
    print(names)

if __name__ == '__main__':
    main3()

my_list = [9,1,0,2,8,6,7,4,5,3]
print('Original order:', my_list)

my_list.sort()
print('Sorted order:',my_list)

my_list = ['beta','alpha','delta','gamma']
print('Original order:', my_list)

my_list.sort()
print('Sorted order:',my_list)
 
# This program demostrates how to use the 'remove' method
# to remove an item from a list.
def main4():
    food = ['Pizza','Burgers','Chips']
    print('Here are the items in the food list:')
    print(food)
    item = input('Which item should I remove? ')
    try:
        food.remove(item)
        print('Here is the revised list:')
        print(food)
    except ValueError:
        print('That item was not found in the list.')

if __name__ == '__main__':
    main4()

my_list = [1,2,3,4,5]
print('Original order:',my_list)

my_list.reverse()
print('Reversed:',my_list)

my_list = [1,2,3,4,5]
print('Before deletion:',my_list)

# del my_list(2)
# print('After deletion:',my_list)

# The 'min' and 'max' function (section)
my_list = [5,4,3,2,50,40,30]
print('The lowest value is', min(my_list))

my_list = [5,4,3,2,50,40,30]
print('The highest value is', max(my_list))
