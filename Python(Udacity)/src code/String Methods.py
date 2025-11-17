# Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling(opens in a new tab). Remember, \n is a special sequence of characters that causes a line break (a new line).

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)


#     What is the length of the string variable verse?
#     What is the index of the first occurrence of the word 'and' in verse?
#     What is the index of the last occurrence of the word 'you' in verse?
#     What is the count of occurrences of the word 'you' in the verse?

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

print(len(verse))
print(verse.find('and'))
print(verse.rfind('you'))
print(verse.count('you'))

print("The length of the string variable verse is {}".format(len(verse)))
print("The index of the first occurrence of the word 'and' in verse is {}".format(verse.find('and')))
print("The index of the last occurrence of the word 'you' in verse is {}".format(verse.rfind('you')))
print("The count of occurrences of the word 'you' in the verse is {}".format(verse.count('you')))
