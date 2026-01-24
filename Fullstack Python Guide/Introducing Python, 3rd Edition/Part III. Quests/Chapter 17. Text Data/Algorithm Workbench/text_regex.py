# When you’re working with text, regular expressions come in handy. We’ll apply them in numerous ways to our featured text sample. It’s a poem titled “Ode on the Mammoth Cheese,” written by James McIntyre in 1866 in homage to a seven-thousand-pound cheese that was crafted in Ontario and sent on an international tour. If you’d rather not type all of it, use your favorite search engine and cut and paste the words into your Python program, or just grab it from Project Gutenberg. Call the text string mammoth.
mammoth = """We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.
Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.
We'rt thou suspended from baloon,
You'd caste a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon."""

# Import the re module to use Python’s regular expression functions. Use re.findall() to print all the words that begin with c.
import re
words_with_c = re.findall(r'\b[cC]\w*', mammoth)
print(words_with_c)

# Find all four-letter words that begin with c.
four_letter_words_begin_c = re.findall(r'[cC]\w{3}\b', mammoth)
print(four_letter_words_begin_c)

# Find all the words that end with r.
end_with_r = re.findall(r'\b\w*[r]\b', mammoth)
print(end_with_r)

# Find all the words that contain exactly three vowels in a row.
three_vowels_row = re.findall(r'\b\w*(?<![aeiou])[aeiou]{3}(?![aeiou])\w*\b', mammoth)
print(three_vowels_row)
