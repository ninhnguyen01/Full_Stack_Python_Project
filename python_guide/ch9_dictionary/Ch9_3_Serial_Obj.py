# Serializing Objects

# serialized (pickling)- converted to bytes in a file

# pickle module 
# 1) open file
# 2) dump method (write)
# 3) close file

# outputfile = open('mydata.dat','wb')
# pickle.dump(object,file)

import pickle
phonebook = {'Chris':'555-1111',
            'Katie':'555-2222',
            'Joanne':'555-3333'}
output_file = open('ch9_dictionary_Python/data/phonebook.dat','wb')
pickle.dump(phonebook, output_file)
output_file.close()

# input_file = open('mydata.dat','rb')
# object = pickle.load(file)

# read past end of file, EOFError exception
input_file = open('ch9_dictionary_Python/data/phonebook.dat','rb')
pb = pickle.load(input_file)
print(pb)
input_file.close()

# This program demonstrates object pickling.
def main_pick():
    again = 'y'
    output_file = open('ch9_dictionary_Python/data/info.dat','wb')
    while again.lower() == 'y':
        save_data(output_file)
        again = input('Enter more data?(y/n): ')
    output_file.close()

def save_data(file):
    person = {}
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    pickle.dump(person,file)    

main_pick()

# This program demonstrates object unpickling.
def main_unpick():
    end_of_file = False
    input_file = open('ch9_dictionary_Python/data/info.dat','rb')
    while not end_of_file:
        try:
            person = pickle.load(input_file)
            display_data(person)
        except EOFError:
            end_of_file = True
    input_file.close()

def display_data(person):
    print('Name:', person['name'])
    print('Age:',person['age'])
    print('Weight:',person['weight'])
    print()

main_unpick()
