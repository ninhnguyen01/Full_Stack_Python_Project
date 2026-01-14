# Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}

# Using your three-word dictionary e2f, print the French word for walrus.
print(e2f.get("walrus"))

# Make a French-to-English dictionary called f2e from e2f. Use the items() method.
f2e = e2f
print(f2e.items())

# Print the English equivalent of the French word chien.
for k in f2e.items():
    if "chien" in k:
        print(k)

# Print the set of English words from e2f.
print(e2f.keys())
