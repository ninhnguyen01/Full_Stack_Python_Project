# Serializing Objects (Title)

# serialized (pickling)- converted to bytes in a file
# pickle module 
# 1) open file
# 2) dump method (write)
# 3) close file

# outputfile = open('mydata.dat','wb')
# pickle.dump(object,file)

# 9.35 What is object serialization?
""" The process of converting the object to a stream of bytes that
can be saved to a file for later retrieval. """

# 9.36 When you open a file for the purpose of saving a pickled
# object to it, what file access mode do you use?
""" A. 'wb' """

# 9.37 When you open a file for the purpose of retrieving a pickled
# object to it, what file access mode do you use?
""" 'rb' """

# 9.38 What module do you import if you want to pickle objects?
""" The pickle module """

# 9.39 What function do you call to pickle an object?
""" pickle.dump """

# 9.40 What function do you call to retrieve and unpickle
# an object?
""" pickle.load """

import pickle
phonebook = {'Chris':'555-1111',
            'Katie':'555-2222',
            'Joanne':'555-3333'}
output_file = open('phonebook.dat','wb')
pickle.dump(phonebook, output_file)
output_file.close()

# input_file = open('mydata.dat','rb')
# object = pickle.load(file)

# read past end of file, EOFError exception
import pickle
input_file = open('phonebook.dat','rb')
pb = pickle.load(input_file)
print(pb)
input_file.close()

# This program demonstrates object pickling.
import pickle
def main():
    again = 'y'
    output_file = open('info.dat','wb')
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

if __name__ == '__main__':
    main()

# This program demonstrates object unpickling.
import pickle
def main():
    end_of_file = False
    input_file = open('info.dat','rb')
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

if __name__ == '__main__':
    main()
