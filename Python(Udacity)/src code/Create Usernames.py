# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for n in names:
    usernames.append(n.lower().replace(' ','_'))

print(usernames)

usernames2 = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames2)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)

