""" Reading Data from a File """
# 'read' method - returns file's contents as a string.
def main():
    infile = open('ch6_file/text/philosopers.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

if __name__ == '__main__':
    main()