""" Concatenating a Newline to a String """
# This program gets three names from the user and writes
# them to a file.
def main():
    print('Enter the names of friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    myfile = open('ch6_file/text/friends.txt','w')
    myfile.write(name1+'\n')
    myfile.write(name2+'\n')
    myfile.write(name3+'\n')
    myfile.close()
    print('The names were written to friends.txt.')

# Alternate with F-strings
    name4 = input('Friend #4: ')
    name5 = input('Friend #5: ')
    name6 = input('Friend #6: ')
    
    myfile = open('ch6_file/text/friends.txt','a')
    myfile.write(f'{name4}\n')
    myfile.write(f'{name5}\n')
    myfile.write(f'{name6}\n')
    myfile.close()
    print('The names were added to friends.txt.')

if __name__ == '__main__':
    main()