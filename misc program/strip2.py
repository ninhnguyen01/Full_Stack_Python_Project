import string

whitespace = string.whitespace
punctuation = string.punctuation
print(punctuation)

blurt = "   What the ...!!?"
clean = blurt.strip(whitespace + punctuation)
print(clean)
