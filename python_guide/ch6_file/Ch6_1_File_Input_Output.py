# Introduction to File Input and Output

#  Three Steps

# OPEN THE FILE
# PROCESS THE FILE (input or output)
# CLOSE THE FILE

""" Types of Files """
# text (ASCII or Unicode) 
# Example -> '.txt'
# binary 
# Example -> '.dat'

""" File Access Methods """
# sequential access file (beginning to end)
# direct access file (jump straight to file)
# [AKA random access file]

""" Filenames and File Objects """
# file object - an object that is associated with a specific
# file and provides a way for the program to work with that 
# file.
# A variable references the file object.

""" Opening a File """
# General Format 'open' Function:
# file_variable = open(filename, mode)

# Python file Modes
# 'r' (to read) [no change or writing]
# 'w' (to write) [file exist, erase, 
# or file no exist, create file]
# 'a' (to append) [file no exist, create file]

customer_file = open('ch6_file/text/customers.txt', 'w')
# General Format Write Method:
# file_variable.write(string)
customer_file.write('Charles Pace ')

# alternate
name = 'Charles Pace2 ' 
customer_file.write(name)
customer_file.close()
