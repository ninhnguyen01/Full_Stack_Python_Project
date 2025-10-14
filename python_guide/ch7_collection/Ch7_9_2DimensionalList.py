# Two_Dimensional Lists

# Reading
students = [['Joe','Kim'],['Sam','Sue'],['Kelly','Chris']]
print(students)
print(students[0])
print(students[1])
print(students[2])

# This program demonstrates a two-dimensional list (nested list)
def list_2d():
    values = [[1,2,3],
              [10,20,30],
              [100,200,300]]
    for row in values:
        for element in row:
            print(element)

list_2d()

# This program assigns random numbers to a 
# two-dimensional list.
# assign value to element with index
import random

ROWS = 3
COLS = 4

def random_2d_list():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,100)
    print(values)

random_2d_list()
