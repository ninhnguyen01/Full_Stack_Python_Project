# Write a function called pointless() that accepts a dict of string:int elements, capitalizes the key, adds 1 to the value, and prints both. Add complete type hints.
def pointless():
    test: dict[str:int] = {
        "Number": 1,
        "Number2": 2,
        "Number3": 3
    }

    print(test)

pointless()
