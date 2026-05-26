# List Methods and Useful Built-in Functions

# The 'append' Method (section)
# add items to a list

# This program demonstrates how the append method can be used 
# to add items to a list

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

# The 'index' Method (section)
# to know if an item is in a list and to locate
 
# This program demonstrates how to get the index of an item
# in a list and then replace that item with a new item.

def main():
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
    main()

# The 'insert' Method (section)
# insert an item at a specific position

# This program demonstrates the 'insert' method.
def main():
    names = ['James','Kathryn','Bill']
    print('The list before the insert:')
    print(names)

    names.insert(0,'Joe')
    print('The list after the insert:')
    print(names)

if __name__ == '__main__':
    main()

# The 'sort' Method (section)
# rearrange elements in a list (low to high)

my_list = [9,1,0,2,8,6,7,4,5,3]
print('Original order:', my_list)

my_list.sort()
print('Sorted order:',my_list)

my_list = ['beta','alpha','delta','gamma']
print('Original order:', my_list)

my_list.sort()
print('Sorted order:',my_list)

# The 'remove' Method (section)
# remove an item from list
 
# This program demostrates how to use the 'remove' method
# to remove an item from a list.
def main():
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
    main()

# The 'reverse' Method (section)
# reverse order of item in list

my_list = [1,2,3,4,5]
print('Original order:',my_list)

my_list.reverse()
print('Reversed:',my_list)

# The 'del' statement (section)
# delete element from a specific index
my_list = [1,2,3,4,5]
print('Before deletion:',my_list)

# del my_list(2)
print('After deletion:',my_list)

# The 'min' and 'max' function (section)
my_list = [5,4,3,2,50,40,30]
print('The lowest value is', min(my_list))

my_list = [5,4,3,2,50,40,30]
print('The highest value is', max(my_list))
