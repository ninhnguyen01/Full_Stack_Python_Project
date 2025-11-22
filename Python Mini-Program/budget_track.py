# Budget Analysis Program
expense = 'Y'
max_budget = 1000.00
total_budget = 0

while expense == 'Y' :
    budget = float(input('Enter your expense for the month: '))
    total_budget += budget
    print(total_budget)
    expense = str(input('Do you have more expenses to add?' +
    " If yes, enter 'Y': ")).upper()

if total_budget <= max_budget:
    print('You are under budget')
else:
    print('You are over budget!')
