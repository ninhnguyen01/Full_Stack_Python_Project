# List Slicing

# slices - selecting subsections of a sequence 
#  
# List Slice general format
# list_name [start : end]

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
'Thursday', 'Friday', 'Saturday']

mid_days = days[2:5]
print(mid_days)

numbers = [1,2,3,4,5]
print(numbers)
print(numbers[1:3])

# no 'start' index, Python uses 0
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[:3])

# no 'end' index, Python uses length of list
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[2:])

# no 'start' or 'end' index, get a copy of the entire list
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[:])

# with step value
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[1:8:2])

# negative numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[-5:])
