# 5. Modify file to add all the numbers read from
# file and displays their total.
infile = open('Starting Out with Python/ch6-file/algorithm-workbench/number_list.txt','r')
file_content_num = infile.read()
total = 0
for num in range (1,101):
    total += num
infile.close()
print(f'The total is: {total}')