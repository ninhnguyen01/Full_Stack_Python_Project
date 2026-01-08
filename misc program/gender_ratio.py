# Male and Female percentages calculation 

males = int(input('Enter the number of males: '))
females = int(input('Enter the number of females: '))

total = males + females

percent_male = males / total
percent_females = females / total

gender_ratio = f'Total people: {total}. Percent males: {percent_male:.0%} & Percent females: {percent_females:.0%}'
gender_ratio

