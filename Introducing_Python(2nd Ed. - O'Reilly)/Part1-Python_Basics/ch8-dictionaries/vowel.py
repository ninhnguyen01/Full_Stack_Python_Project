vowels = 'aeious'
word = 'onomatopoeia'

vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)