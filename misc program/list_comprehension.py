num_list = [num for num in range(1,6)] # expression for item in iterable if condition

print(num_list)

num_list2 = [num for num in range(1,6) if num % 2 == 0] # expression for item in iterable if condition

print(num_list2)

list_of_num = []
for num in range(1,6): # expression for item in iterable if condition
    if num % 2 == 1:
        list_of_num.append(num)    
print(list_of_num)