# Tuples (Title)

# tuple
my_tuple = (1,2,3,4,5)
print(my_tuple)

# tuple with 'for' loop
names = ('Holly','Warren','Ashley')
for n in names:
    print(n)

#  Tuples Index
names = ('Holly','Warren','Ashley')
for i in range(len(names)):
    print(names[i])

# One Element Tuple
# my_tuple = (1,)

# Converting between Lists and Tuples 
number_tuple = (1,2,3)
number_list = list(number_tuple)
print(number_list)

str_list = ['one','two','three']
str_tuple = tuple(str_list)
print(str_tuple)
