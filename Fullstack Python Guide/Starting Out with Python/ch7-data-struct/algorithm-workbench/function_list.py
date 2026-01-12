# Write a function that accepts a list as an argument
# (assume the list contains integers) and returns the total
# of the values in the list.

def list_sum():
    list1 = [10, 20, 30, 40, 50]
    total = 0
    for i in list1:
        total += i
    print(f'The total of the elements is {total}.')
    
list_sum()