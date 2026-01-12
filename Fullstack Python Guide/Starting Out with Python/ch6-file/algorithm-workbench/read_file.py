# Write a program that opens the my_name.txt file,
# ...read name from file, displays name, closes file.
infile = open('Starting Out with Python/ch6-file/algorithm-workbench/my_name.txt','r')
file_content_name = infile.read()
infile.close()
print(file_content_name)
