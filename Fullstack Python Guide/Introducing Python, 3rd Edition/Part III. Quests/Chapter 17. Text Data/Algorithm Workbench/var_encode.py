# Create a Unicode string called mystery and assign it the value \U0001f984. Print mystery and its Unicode name. Then assign \U0001f4a9 to mystery2 and do the same. (Your system font may or may not display an image for both.)
import unicodedata

mystery = '\U0001f984'
print(f'Unicode Name: {unicodedata.name(mystery)}')
print(f'Unicode Symbol: {mystery}')

mystery2 = '\U0001f4a9'
print(f'Unicode Name: {unicodedata.name(mystery2)}')
print(f'Unicode Symbol: {mystery2}')

# Encode mystery, this time using UTF-8, into the bytes variable pop_bytes. Print pop_bytes.
pop_bytes =  mystery.encode('UTF-8')
print(pop_bytes)

# Using UTF-8, decode pop_bytes into the string variable pop_string. Print pop_string. Is pop_string equal to mystery?
pop_string = pop_bytes.decode('UTF-8')
print(pop_string)
if pop_string == mystery:
    print("pop_string equal to mystery")
else:
    print("pop_string NOT equal to mystery")
