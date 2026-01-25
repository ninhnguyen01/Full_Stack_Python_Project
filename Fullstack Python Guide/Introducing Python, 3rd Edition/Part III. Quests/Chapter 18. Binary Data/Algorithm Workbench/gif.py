# Use unhexlify() to convert this hex string (combined from two strings to fit on a page) to a bytes variable called gif:

# '47494638396101000100800000000000ffffff21f9' +
# '0401000000002c000000000100010000020144003b'

import binascii as ba

gif = ba.unhexlify('47494638396101000100800000000000ffffff21f9' +
'0401000000002c000000000100010000020144003b')
print(gif)

# The bytes in gif define a 1-pixel transparent GIF file, one of the most common graphics file formats. A legal GIF starts with the string GIF89a. Does gif match this?
