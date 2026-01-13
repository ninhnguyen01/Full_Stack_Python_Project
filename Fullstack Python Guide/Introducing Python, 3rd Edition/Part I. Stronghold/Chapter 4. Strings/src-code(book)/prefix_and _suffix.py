# You may need to find, change, or delete the prefix or suffix of a string. 
# If this never happens to you, feel free to make yourself a sandwich now. 
# Otherwise, here are a few useful Python string methods:

s = "inconceivable"
print(s.startswith("in"))

print(s.startswith("un"))

print(s.endswith("able"))

print(s.endswith("abominable"))

print(s.removeprefix("in"))

print(s.removesuffix("conceivable"))

# To add a prefix or suffix, use + to concatenate (join) the old word and the new part:
print("ultra" + s)
print(s + "ness")
