# This program writes three lines of data to a file.
def main():
    outfile = open('ch6_file/text/philosopers.txt', 'w')
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close()

if __name__ == '__main__':
    main()