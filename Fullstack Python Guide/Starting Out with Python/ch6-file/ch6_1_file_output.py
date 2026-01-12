# Introduction to File Input and Output (Title)

#  Three Steps:
# OPEN THE FILE
# PROCESS THE FILE (input or output)
# CLOSE THE FILE

# Types of Files (section)
# text (ASCII or Unicode) 
# Example -> '.txt'
# binary 
# Example -> '.dat'

# File Access Methods 
# sequential access file (beginning to end)
# direct access file (jump straight to file)
# [ AKA random access file ]

# Filenames and File Objects 
# file object - an object that is associated with a specific
# file and provides a way for the program to work with that file.
# A variable references the file object.

# Opening a File 
# General Format 'open' Function:
# file_variable = open(filename, mode)

# Python file Modes
# 'r' (to read) [no change or writing]
# 'w' (to write) [file exist, erase, 
# or file no exist, create file]
# 'a' (to append) [file no exist, create file]

# General Format Write Method:
""" file_variable.write(string) """

# int and float functions ignore any \n at the end of the 
# string that is passed as an argument.

# 6.1 What is an output file?
""" A file to which a program writes data. It is called an output
# file because the program sends output to it. """
 
# 6.2 What is an input file?
""" A file from which a program reads data. It is called an input
file because the program receives input from it. """

# 6.3 What three steps must be taken by a program when it uses a
# file? 
""" (1) Open the file. (2) Process the file. (3) Close the file. """

# 6.4 In general, what are the two types of files? What is the 
# difference between these two types of files?
""" Text and binary. Test file is encoded using ASCII (set of 
# characters). Binary file is nontext and you cannot view with
# text editor. """

# 6.5 What are the two types of file access? What is the difference
# between these two?
""" Sequential and direct access. Sequential is data access from
beginning of file to end. Direct is jumping to the data without
reading any that comes before it. """

# 6.6 When writing a program that performs an operation on a file, what
# two file-associated names do you have to work with in your code?
""" The file's name and the name of a variable that references a 
# file object. """

# 6.7 If a file already exists, what happens to it if you try 
# to open it as an output file (using the 'w' mode)?
""" The file's content are erased. """

# 6.8 What is the purpose of opening a file?
""" Opening a file creates a connection between the file and
# the program. It also creates an association between the file 
# and a file object. """

# 6.9 What is the purpose of closing a file?
""" Closing a file disconnects the program from the file. """

# 6.10 What is a file's read position? Initially, where is the
# read position when an input file is opened?
""" A file's read position marks the location of the next item
# that will be read from the file. When an input file is opened, 
# its read position is initially set to the first item in the file. """

# 6.11 In what mode do you open a file if you want to write data to it, but
# you do not want to erase the file's existing contents? When you
# write data to such a file, to what part of the file is the data 
# written?
""" You open the file in append mode. When you write data to a 
# file in append mode,the data is written to the end of the file's
# existing contents. """

customer_file = open('customers.txt', 'w')
sales_file = open('sales.txt', 'w')

# Specifying a location of a file 
test_file = open('test.txt','w')

# Writing Data to a File 
# method - a function that belongs to an object
# and performs some operation using that object.
customer_file = open('customers.txt','w')

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

# Reading Data from a File 
# 'read' method - returns file's contents as a string.
def main2():
    infile = open('philosopers.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

if __name__ == '__main__':
    main2()

# This program reads the contents of the philosophers.txt
# file one line at a time.
def main3():
    infile = open('philosopers.txt', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    infile.close()
    print(line1)
    print(line2)
    print(line3)

if __name__ == '__main__':
    main3()

# Concatenating a Newline to a String 
# This program gets three names from the user and writes
# them to a file.
def main4():
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
"""
    myfile.write(f'{name1}\n')
    myfile.write(f'{name2}\n')
    myfile.write(f'{name3}\n')
"""

if __name__ == '__main__':
    main4()

# Reading a String and Stripping the Newline from It 
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
def main5():
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
    main5()

# Appending Data to an Existing File 
    myfile = open('friends.txt','a')
    myfile.write('A\n')
    myfile.write('B\n')
    myfile.write('C\n')
    myfile.close()

# Writing and Reading Numeric Data 
# This program demonstrates how numbers must be converted
# to strings before they are written to a text file.

def main6():
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
    main6()

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

# This program demonstrates how numbers that are read from
# a file must be converted from strings before they are
# used in a math operation.
def main7():
    infile = open('numbers.txt','r')
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    infile.close()

    total = num1 + num2 + num3
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')
    
if __name__ == '__main__':
    main7()
