from collections import OrderedDict
# Make a dictionary called plain with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and then print it.
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# Make an OrderedDict called fancy from the same pairs listed in the previous question and print it. Did it print in the same order as plain?
fancy = OrderedDict(plain)
print(fancy)
