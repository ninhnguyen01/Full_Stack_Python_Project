# Two_Dimensional Lists (Title)

students = [['Joe','Kim'],['Sam','Sue'],['Kelly','Chris']]
print(students)
print(students[0])
print(students[1])
print(students[2])

# This program demonstrates a two-dimensional list (nested list)
def main():
    values = [[1,2,3],
              [10,20,30],
              [100,200,300]]
    for row in values:
        for element in row:
            print(element)

if __name__ == '__main__':
    main()

# This program assigns random numbers to a 
# two-dimensional list.
# assign value to element with index
import random

ROWS = 3
COLS = 4

def main():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,100)
    print(values)

if __name__ == '__main__':
    main()
