hex_string = "FF 01 61 62 63 64 6566"
the_bytes = bytes.fromhex(hex_string)
print(the_bytes)

the_bytes2 = b'\xff\x01abcdef'
hex_string = the_bytes2.hex()
print(hex_string)
