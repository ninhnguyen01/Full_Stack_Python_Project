# Write code that does the following: open outputfile
# with filename number_list.txt, uses a loop to write number 1
# through 100 to the file, closes file.
outputfile = open('Starting Out with Python/ch6-file/algorithm-workbench/number_list.txt','w')
for num in range (1,101):
    outputfile.write(str(num)+'\n')
outputfile.close()