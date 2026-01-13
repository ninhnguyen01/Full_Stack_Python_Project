# The id is unique for each object in memory. 
# Although the Python interpreter may use just the object’s location in memory, don’t assume this. 
# The important point is that the id is unique. The id() function returns the unique ID:

x = 5
print(id(x))
x = 6
print(id(x))

