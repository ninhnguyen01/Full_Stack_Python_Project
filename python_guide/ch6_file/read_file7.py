# int and float functions ignore any \n at the end of the 
# string that is passed as an argument.

# This program demonstrates how numbers that are read from
# a file must be converted from strings before they are
# used in a math operation.
def main():
    infile = open('ch6_file/text/numbers.txt','r')
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    infile.close()

    total = num1 + num2 + num3
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')
    
if __name__ == '__main__':
    main()