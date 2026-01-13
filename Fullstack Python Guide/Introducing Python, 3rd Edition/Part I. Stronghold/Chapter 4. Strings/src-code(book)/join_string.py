# Not too surprisingly, the join() function is the opposite of split(): it collapses a list of strings into a single string. 
# The join() function looks a bit backward because you specify the string that glues everything together first and then the list of strings to glue: string .join( list ). 
# So, to join the list lines with separating newlines, you would write '\n'.join(lines). 
# As you’ll see in Chapter 8, one way to make a list is with square brackets ([ and ]) surrounding a comma-separated sequence of items. 
# In the following example, let’s join some names in a list with a comma and a space:

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
