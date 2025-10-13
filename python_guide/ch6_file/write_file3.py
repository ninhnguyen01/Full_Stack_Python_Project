""" Writing and Reading Numeric Data """
# This program demonstrates how numbers must be converted
# to strings before they are written to a text file.

def main():
    outfile = open('ch6_file/text/numbers.txt','w')
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    outfile.write(str(num1)+'\n')
    outfile.write(str(num2)+'\n')
    outfile.write(str(num3)+'\n')

    outfile.close()
    print('Data written to numbers.txt')

if __name__ == '__main__':
    main()