days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]

drinks = [
    'coffee',
    'tea',
    'beer',
    'coffee',
    'coffee'
]

for day, drink in zip(days, drinks):
    print('Day:', day, '|', 'Drink -->', drink)