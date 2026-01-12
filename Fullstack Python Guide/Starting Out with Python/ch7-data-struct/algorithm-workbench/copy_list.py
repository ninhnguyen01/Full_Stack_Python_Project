# 3. Assume the list 'numbers1' has 100 elements, and
# 'numbers2' is an empty list. Write code that copies
# the values in 'numbers1' to 'numbers2'.

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = []
numbers2 = numbers1
print(numbers2)

numbers2 = numbers1.copy()
print(numbers2)
