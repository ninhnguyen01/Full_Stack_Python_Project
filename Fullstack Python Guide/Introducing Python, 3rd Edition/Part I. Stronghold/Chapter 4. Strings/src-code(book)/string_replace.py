# You use replace() for simple substring substitution. 
# Give it the old substring, the new one, and the number of instances of the old substring to replace. 
# The function returns the changed string but does not modify the original. 
# If you omit this final count argument, join() replaces all instances. 
# In this example, only one string (duck) is matched and replaced in the returned string:

setup = "a duck goes into a bar..."
print(setup)
animal = setup.replace('duck', 'marmoset')
print(animal)
change_all = setup.replace('a ', 'a famous ')
print(change_all)
