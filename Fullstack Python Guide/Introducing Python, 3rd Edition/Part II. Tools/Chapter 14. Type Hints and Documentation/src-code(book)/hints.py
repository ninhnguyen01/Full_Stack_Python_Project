palindrome: str = "Was it a car or a cat I saw?"
print(type(palindrome))

# For collection types like list, tuple, and dict, you can specify which types are in the collection:
# name: dict[keytype, valtype] = {key1: val1, key2: val2}
nays: dict[str, str] = {
    "horse": "neigh",
    "pedant": "nay!",
    "genealogist": "n\N{LATIN SMALL LETTER E WITH ACUTE}e"
}

# Hints apply to function parameters and return values.
def num_to_str(num: int) -> str:
    return str(num)

print(num_to_str(5))
print(type(num_to_str(5)))

def no_return(num: int) -> None:
    print("Hey, got a", num)

print(no_return(1))    
print(type(no_return(1)))
