import pickle
import ch10_OOP_Python.cellphone.cellphone as cellphone

FILENAME = 'cellphones.dat'
def main():
    again = 'y'
    output_file = open(FILENAME,'wb')
    while again.lower() == 'y':
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))
        phone = cellphone.Cellphone(man,mod,retail)
        pickle.dump(phone,output_file)
        again = input('Enter more phone data? (y/n): ')
    output_file.close()
    print(f'The data was written to {FILENAME}.')

if __name__ == '__main__':
    main()