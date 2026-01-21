# Install pip if you don’t have it. Make pip install the pyspellchecker package.
# Read the pyspellchecker docs at the PyPI and Read the Docs websites. Write a small script that takes a list of words, reports whether any are misspelled, and reports the likely true spelling. Note that more than 10 languages are supported.
from spellchecker import SpellChecker

spell = SpellChecker(language='de') # use the German Dictionary
spell.word_frequency.load_text_file('Part II. Tools/Chapter 13. Development Environment/Algorithm Workbench/aufsatz.txt')

print([spell.known(word.split(' ')) for word in spell])

# could add command line arguments to set the parameters of the spell
# check class; setup what type of information to present back, etc.
print("To exit, hit return without input!")
while True:
    word = input('Input a word to spell check: ')
    if word == '':  # not sure, but need a way to kill the program...
        break
    if word in spell:
        print("'{}' is spelled correctly!".format(word))
    else:
        cor = spell.correction(word)
        print("The best spelling for '{}' is '{}'".format(word, cor))

        print("If that is not enough; here are all possible candidate words:")
        print(spell.candidates(word))
