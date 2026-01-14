word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

# for loop
for letter in word:
    print(letter)

word = 'thunor'
for letter in word:
     if letter == 'u':
         break
     print(letter)

word = 'donar'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")     
    