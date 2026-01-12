# Write code that does the following: opens number_list.txt file,
# read numbers from file, displays them, 
# closes file.
infile = open('Starting Out with Python/ch6-file/algorithm-workbench/number_list.txt','r')
file_content_num = infile.read()
infile.close()
print(file_content_num)