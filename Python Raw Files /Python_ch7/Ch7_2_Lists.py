# Introduction to Lists (Title)

# Reading

# list
even_numbers = [2, 4, 6, 8, 10]
names = ['Molly', 'Steven', 'Will', 'Alicia', 'Adriana']
info = ['Alicia', 27, 1550.87]

numbers = [5, 10, 15, 20]
print(numbers)

numbers = list(range(5))
print(numbers)

numbers = list(range(1,10,2))
print(numbers)

# The Repetition Operator (section) 
# General Format:
# list * n 
numbers = [0] * 5
print(numbers)

numbers = [1,2,3] * 3
print(numbers)

numbers = [1,2,3,4]
for num in numbers:
    print(num)

# no effect on loop
numbers = [1,2,3,4]
for num in numbers:
    num = 99
print(numbers)

# Indexing (section)
# access elements in list with index
my_list = [10,20,30,40]
print(my_list[0],my_list[1],my_list[2],my_list[3])

my_list = [10,20,30,40]
index = 0 
while index < 4:
    print(my_list[index])
    index += 1
    print(index)

my_list = [10,20,30,40]
print(my_list[-1],my_list[-2],my_list[-3],my_list[-4])

# The 'len' Function (section)
# 'Len' return length of a sequence
my_list = [10,20,30,40]
size = len(my_list)
print(size)

my_list = [10,20,30,40]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Using a 'for' loop to Iterate by Index Over a List (section)
names  = ['Jenny', 'Kelly', 'Chloe', 'Aubrey']
for index in range(len(names)):
    print(names[index])

# Lists are Mutable (section)
numbers = [1,2,3,4,5]
print(numbers)
numbers[0] = 99
print(numbers)

# Fill a list with values
numbers = [0] * 5
for index in range(len(numbers)):
    numbers[index] = 99
    print(numbers)

# Sales List
NUM_DAYS = 5

def main():
    sales = [0] * NUM_DAYS
    print('Enter the sales for each day')
    for index in range(len(sales)):
        sales[index]= float(input(f'Day #{index+1}: '))
    print('Here are the values you enter: ')
    for value in sales:
        print(value)

if __name__ == '__main__':
    main()

# Concatenating Lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = list1 + list2
print(list3)

girl_names = ['Joanne', 'Karen', 'Lori']
boy_names = ['Chris', 'Jerry', 'Will']
all_names = girl_names + boy_names
print(all_names)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1 += list2
print(list1)

girl_names = ['Joanne', 'Karen', 'Lori']
girl_names += ['Jenny','Kelly']
print(girl_names)

# concat lists only with other lists.
