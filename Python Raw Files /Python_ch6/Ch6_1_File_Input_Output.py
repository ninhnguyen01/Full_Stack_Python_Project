# Introduction to File Input and Output (Title)

#  Three Steps

# OPEN THE FILE
# PROCESS THE FILE (input or output)
# CLOSE THE FILE

# Types of Files (section)
# text (ASCII or Unicode) 
# Example -> '.txt'
# binary 
# Example -> '.dat'

# File Access Methods (section)
# sequential access file (beginning to end)
# direct access file (jump straight to file)
# [AKA random access file]

# Filenames and File Objects (section)
# file object - an object that is associated with a specific
# file and provides a way for the program to work with that 
# file.
# A variable references the file object.

# Opening a File (section)
# General Format 'open' Function:
# file_variable = open(filename, mode)

# Python file Modes
# 'r' (to read) [no change or writing]
# 'w' (to write) [file exist, erase, 
# or file no exist, create file]
# 'a' (to append) [file no exist, create file]

customer_file = open('customers.txt', 'r')
sales_file = open('sales.txt', 'w')

# Specifying a location of a file (section)
test_file = open('test.txt','w')

# Writing Data to a File (section)
# method - a function that belongs to an object
# and performs some operation using that object.
customer_file = open('customers.txt','w')

# General Format Write Method:
# file_variable.write(string)
customer_file.write('Charles Pace')

# alternate
name = 'Charles Pace' 
customer_file.write(name)

customer_file.close()

# This program writes three lines of data to a file.
def main():
    outfile = open('philosopers.txt', 'w')
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close()

if __name__ == '__main__':
    main()

# Reading Data from a File (section)
# 'read' method - returns file's contents as a string.
def main():
    infile = open('philosopers.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

if __name__ == '__main__':
    main()

# This program reads the contents of the philosophers.txt
# file one line at a time.
def main():
    infile = open('philosopers.txt', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    infile.close()
    print(line1)
    print(line2)
    print(line3)

if __name__ == '__main__':
    main()

# Concatenating a Newline to a String (section)
# This program gets three names from the user and writes
# them to a file.
def main():
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    myfile = open('friends.txt','w')
    myfile.write(name1+'\n')
    myfile.write(name2+'\n')
    myfile.write(name3+'\n')
    myfile.close()
    print('The names were written to friends.txt.')

# Alternate with F-strings
    myfile.write(f'{name1}\n')
    myfile.write(f'{name2}\n')
    myfile.write(f'{name3}\n')

if __name__ == '__main__':
    main()

# Reading a String and Stripping the Newline from It (section)
# rstrip - removes or "strips" specific characters from the 
# end of a string.
name = 'Joanne Manchester\n'
name2 = 'Joanne Manchester2\n'
print(name)
print(name2)

name = 'Joanne Manchester\n'
name = name.rstrip('\n')
name2 = 'Joanne Manchester2\n'
print(name)
print(name2)

# This program reads the contents of the philosophers.txt file
# one line at a time.
def main():
    infile = open('philosopers.txt', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    infile.close()

    print(line1)
    print(line2)
    print(line3)
    
if __name__ == '__main__':
    main()

# Appending Data to an Existing File (section)
    myfile = open('friends.txt','a')
    myfile.write('Andrew\n')
    myfile.write('Bern\n')
    myfile.write('Aiguin\n')
    myfile.close()

# Writing and Reading Numeric Data (section)
# This program demonstrates how numbers must be converted
# to strings before they are written to a text file.

def main():
    outfile = open('numbers.txt','w')
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    outfile.write(str(num1)+'\n')
    outfile.write(str(num2)+'\n')
    outfile.write(str(num3)+'\n')

    outfile.close()
    print('Data written to numbers.txt')

if __name__ == '__main__':
    main()

infile = open('numbers.txt','r')
value = infile.readline()
infile.close()

# string to integer
infile = open('numbers.txt','r')
string_input = infile.readline()
value = int(string_input)
infile.close()

# one statement
infile = open('numbers.txt','r')
value = int(infile.readline())
infile.close()

# int and float functions ignore any \n at the end of the 
# string that is passed as an argument.

# This program demonstrates how numbers that are read from
# a file must be converted from strings before they are
# used in a math operation.
def main():
    infile = open('numbers.txt','r')
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    infile.close()

    total = num1 + num2 + num3
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')
    
if __name__ == '__main__':
    main()
