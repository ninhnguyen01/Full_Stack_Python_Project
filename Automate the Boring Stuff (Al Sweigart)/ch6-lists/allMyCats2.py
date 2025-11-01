cat_name = []

while True:
    print('Enter the name of cat ' + str(len(cat_name) + 1) + ':' +
      ' (Or enter nothing to save)')
    name = input()
    if name == '':
        break
    cat_name += [name]  # List concatenation

with open('ch6-lists/cat_names.txt','w') as c:
    name = c.write(str(cat_name))
    print('Saved to file')
    c.close()