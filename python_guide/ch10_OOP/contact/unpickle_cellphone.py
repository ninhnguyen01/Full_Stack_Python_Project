import pickle
import ch10_OOP_Python.cellphone.cellphone as cellphone

FILENAME = 'cellphones.dat'
def main():
    end_of_file = False
    input_file = open(FILENAME,'rb')
    while not end_of_file:
        try:
            phone = pickle.load(input_file)
            display_data(phone)
        except EOFError:
            end_of_file = True
    input_file.close()
def display_data(phone):
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model Number: {phone.get_model()}')
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')
    print()

if __name__ == '__main__':
    main()