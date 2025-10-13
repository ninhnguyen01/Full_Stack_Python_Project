""" Appending Data to an Existing File """
myfile = open('ch6_file/text/friends.txt','a')
myfile.write('Andrew\n')
myfile.write('Eric\n')
myfile.write('Adler\n')
myfile.close()
