# Save the following text lines to a file called books.csv (notice that if the fields are separated by commas, you need to surround any comma-containing field with quotes):
import csv

text = [['author','book'],
        ['J R R Tolkien','The Hobbit'],
        ['Lynne Truss',"Eats, Shoots & Leaves"]]

with open('books.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(text)
