# Here’s a brief explanation of the pieces of this call:

# fileobj = open( filename, mode )

#     fileobj is the file object returned by open().
#     filename is the string name of the file.
#     mode is a string indicating the file’s type and what you want to do with it.

# The first letter of mode indicates the operation:
#     r means read.
#     w means write. If the file doesn’t exist, it’s created. If the file does exist, it’s overwritten.
#     x means write, but only if the file does not already exist.
#     a means append (write after the end) if the file exists.

# The second letter of mode is the file’s type:
#     t (or nothing) means text.
#     b means binary.

# Here’s a brief explanation of the pieces of this call:

# fileobj = open( filename, mode )
#     fileobj is the file object returned by open().
#     filename is the string name of the file.
#     mode is a string indicating the file’s type and what you want to do with it.

# The first letter of mode indicates the operation:
#     r means read.
#     w means write. If the file doesn’t exist, it’s created. If the file does exist, it’s overwritten.
#     x means write, but only if the file does not already exist.
#     a means append (write after the end) if the file exists.

# The second letter of mode is the file’s type:
#     t (or nothing) means text.
#     b means binary.

fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

import os
print(os.path.exists('oops.txt'))
name = 'oops.txt'
print(os.path.isfile(name))
