# Write a program that opens an output file with the filename
# ...write name to file, close file.
outputfile = open('Starting Out with Python/ch6-file/algorithm-workbench/my_name.txt','w')
name = 'John'
outputfile.write(name)
outputfile.close()
