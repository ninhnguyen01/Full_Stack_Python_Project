# Assume the variable dct references a dictionary. Write
# an 'if' statement that determines whether the key 'Jim'
# exists in the dictionary. If so, delete 'Jim' and 
# its associated value.

dct = {'John': 101, 'James': 202,'Jim': 501}
print(dct)

if 'Jim' in dct:
    del dct['Jim']
    print(dct)