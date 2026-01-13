# Make a bytes variable called b from the integers 1 through 5.
b = bytes(12345)

# Print the length of b.
print(len(b))

# Make a bytearray variable called ba. Or call it sasquatch; it really doesn’t matter. 
# Fill the variable with the integers 1 through 5.
ba = bytearray(12345)

# Print the length of ba (or whatever you called it).
print(len(ba))

# Assign b to ba.
ba = b
print(ba)
print()
print()

# Assign ba to b.
b = ba
print(b)
print()
print()
