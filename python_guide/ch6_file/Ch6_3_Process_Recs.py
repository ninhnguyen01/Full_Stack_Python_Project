# Processing Records

# This program gets employee data from the user
# and saves it as records in the employee.txt file.
def main():
    num_emps = int(input('How many employee records ' +
    'do you want to create? '))
    emp_file = open('ch6_file/text/employees.txt','w')
    for count in range(1,num_emps+1 ):
        print(f'Enter data for employee #{count}')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')

        print()

    emp_file.close()
    print('Employee records written to employees.txt.')

if __name__ == '__main__':
    main()

# This program displays the records that are in
# the employees.txt file.
def main():
    emp_file = open('ch6_file/text/employees.txt','r')
    name = emp_file.readline()
    while name != '':
        
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        print(f'Name: {name}')
        print(f'ID: {id_num}')
        print(f'Dept: {dept}')
        print()

        name = emp_file.readline()

    emp_file.close()

if __name__ == '__main__':
    main()

# This program adds coffee inventory records to the 
# coffee.txt file.
# description -> string
# quantity -> float 
def main():
    another = 'y'
    coffee_file = open('ch6_file/text/coffee.txt','a')
    while another == 'y' or another == 'Y':
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))
        coffee_file.write(descr + '\n')
        coffee_file.write(f'{qty}\n')
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    coffee_file.close()
    print('Data appended to coffee.txt.')

if __name__ == '__main__':
    main()

# This program displays the records in the coffee.txt file.
def main():
    coffee_file = open('ch6_file/text/coffee.txt','r')
    descr = coffee_file.readline()
    while descr != '':
        qty = str(coffee_file.readline())
        descr = descr.rstrip('\n')
        print(f'Description: {descr}')
        print(f'Quantity: {qty}')
        descr = coffee_file.readline()
    
    coffee_file.close()

if __name__ == '__main__':
    main()

# This program allows the user to search the coffee.txt
# file for records matching a description.
def main():
    found = False
    search = input('Enter a description to search for: ')
    coffee_file = open('ch6_file/text/coffee.txt','r')
    descr = coffee_file.readline()

    while descr != '':
        qty = str(coffee_file.readline())
        descr = descr.rstrip('\n')

        if descr == search:
            print(f'Description: {descr}')
            print(f'Quantity: {qty}')
            print()
            found = True

        descr = coffee_file.readline()
    
    coffee_file.close()

    if not found:
        print('That item was not found in the file.')

if __name__ == '__main__':
    main()

# pseudocode
# 1) Open original file for input and creat tmp file for output.
# 2) Get descr of the rec to be modified and new val for quantity.
# 3) Read first descr from original file.
# 4) While descr not empty:
#       read quantity field
#       if this rec descr matches the descr entered:
#           write new data to tmp file
#       else:
#           write existing rec to tmp file
#       read next descr field   
# 5) Close original file and tmp file
# 6) Delete original file
# 7) Rename the tmp file, giving name of original file.

# This program allows the user to modify the quantity in a 
# record in the coffee.txt file.

import os # needed for remove and rename function
def main():
    found = False
    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new quantity: '))
    coffee_file = open('ch6_file/text/coffee.txt','r')
    temp_file = open('ch6_file/text/temp.txt','w')
    descr = coffee_file.readline()
    while descr != '':
        qty = str(coffee_file.readline())
        descr = descr.rstrip('\n')

        if descr == search:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')
            found = True
        else:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        descr = coffee_file.readline()
    
    coffee_file.close()
    temp_file.close()

    os.remove('ch6_file/text/coffee.txt')
    os.rename('ch6_file/text/temp.txt', 'ch6_file/text/coffee.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

if __name__ == '__main__':
    main()

# pseudocode
# 1) Open original file for input and creat tmp file for output.
# 2) Get descr of the rec to be deleted.
# 3) Read first rec descr in the original file.
# 4) While descr not empty:
#       read quantity field
#       if this rec descr no matches the descr entered:
#           write rec to tmp file
#       read next descr field
# 5) Close original file and tmp file
# 6) Delete original file
# 7) Rename the tmp file, giving name of original file.

# This program allows the user to delete a record in the 
# coffee.txt file.
import os # needed for remove and rename function
def main():
    found = False
    search = input('Which coffee do you want to delete? ')
    coffee_file = open('ch6_file/text/coffee.txt','r')
    temp_file = open('ch6_file/text/temp.txt','w')
    descr = coffee_file.readline()
    while descr != '':
        qty = str(coffee_file.readline())
        descr = descr.rstrip('\n')

        if descr != search:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')
        else:
            found = True

        descr = coffee_file.readline()
    
    coffee_file.close()
    temp_file.close()

    os.remove('ch6_file/text/coffee.txt')
    os.rename('ch6_file/text/temp.txt', 'ch6_file/text/coffee.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

if __name__ == '__main__':
    main()

""" Note ---

- What is a record? What is a field?
A record is a complete set of data that describes one item,
and a field is a single piece of data within a record.

- Describe a way that you use a temporary file in a progam 
that modifies a record in a sequential access file. 
You copy all the original file's records to the temporary file,
but when you get to the record that is to be modified, you do not
write its old contents to the temporary file. Instead, you write
its new, modified values to the temporary file. Then, you finish
copying any remaining records from the original file to the 
temporary file.

- Describe the way that you use a temporary file in a program
that deletes a record from a sequential file.
You copy all the original file's records to the temporary file,
except for the record that is to be deleted. The temporary file
then takes the place of the original file. You delete the 
original file and rename the temporary file, giving it the name
that the original file had on the computer's disk.
 
"""