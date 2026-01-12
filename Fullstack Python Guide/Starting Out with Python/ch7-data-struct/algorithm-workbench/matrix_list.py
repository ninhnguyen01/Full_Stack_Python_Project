# Write a statement that creates a two-dimensional list
# with 5 rows and 3 columns. Then write nested loops that get
# an integer value from the user for each element in the list.
list1 = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,12,13],
         [14,15,16]]

for a in list1:
    for b in list1:
        print(a, b)
