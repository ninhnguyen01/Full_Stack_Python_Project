# List Methods and Useful Built-in Functions

# list methods
# ------------
# append(item)
# index(item)
# insert(index,item)
# sort()
# remove(item)
# reverse()

""" The 'append' Method """
# add items to a list

# This program demonstrates how the append method can be used 
# to add items to a list

def add_name():
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

add_name()

""" The 'index' Method """
# to know if an item is in a list and to locate
 
# This program demonstrates how to get the index of an item
# in a list and then replace that item with a new item.

def item_change():
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

item_change()

""" The 'insert' Method """
# insert an item at a specific position

# This program demonstrates the 'insert' method.
def guest_list():
    names = ['James','Kathryn','Bill']
    print('The list before the insert:')
    print(names)

    names.insert(0,'Joe')
    print('The list after the insert:')
    print(names)

guest_list()

""" The 'sort' Method """
# rearrange elements in a list (low to high)

my_list = [9,1,0,2,8,6,7,4,5,3]
print('Original order:', my_list)

my_list.sort()
print('Sorted order:',my_list)

my_list = ['beta','alpha','delta','gamma']
print('Original order:', my_list)

my_list.sort()
print('Sorted order:',my_list)

""" The 'remove' Method """
# remove an item from list
 
# This program demostrates how to use the 'remove' method
# to remove an item from a list.
def food_list():
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

food_list()

""" The 'reverse' Method """
# reverse order of item in list

my_list = [1,2,3,4,5]
print('Original order:',my_list)

my_list.reverse()
print('Reversed:',my_list)

""" The 'del' statement """
# delete element from a specific index
my_list2 = [1,2,3,4,5]
print('Before deletion:',my_list2)

del my_list2[2]
print('After deletion:',my_list2)

""" The 'min' and 'max' function """
my_list3 = [5,4,3,2,50,40,30]
print('The lowest value is', min(my_list3))

my_list3 = [5,4,3,2,50,40,30]
print('The highest value is', max(my_list3))

""" Note -- 

- What is the difference between calling a list's 'remove' 
method and using the 'del' statement to remove an element? 

The remove method searches for and removes an element 
containing a specific value. The del statement removes an element
at a specific index. 

"""