# Male and Female Percentages Program
males = int(input('Enter the number of males: '))
females = int(input('Enter the number of females: '))

total = males + females

percent_male = males / total
percent_females = females / total

print(f'percent males:{percent_male:.0%}')
print(f'percent females:{percent_females:.0%}')
