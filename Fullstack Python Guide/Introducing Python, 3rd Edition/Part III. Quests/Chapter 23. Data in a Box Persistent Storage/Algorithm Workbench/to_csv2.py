# Create a CSV file called books2.csv by using these lines:
import csv

text = [['title','author','year'],
['The Weirdstone of Brisingamen','Alan Garner',1960],
['Perdido Street Station','China Miéville',2000],
['Thud!','Terry Pratchett',2005],
['The Spellman Files','Lisa Lutz',2007],
['Small Gods','Terry Pratchett',1992]]

with open('books2.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(text)
