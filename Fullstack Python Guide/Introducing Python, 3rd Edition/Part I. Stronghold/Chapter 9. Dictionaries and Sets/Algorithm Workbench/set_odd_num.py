# Use a set comprehension to create the set odd from the odd numbers in range(10).
odd_set = {o for o in set(range(10)) if o % 2 != 0}
print(odd_set)
