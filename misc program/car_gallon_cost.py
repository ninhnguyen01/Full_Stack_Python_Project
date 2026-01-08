# Estimation of maximum cost for car by gallon

price_per_gallon = float(input('Enter the cost of each gallon in $: '))
total_car_gallon = float(input('Enter the total amount of gallons for your car: '))
max_cost = price_per_gallon * total_car_gallon
max_dist = f'It costs ${max_cost} for {total_car_gallon} gallon for your car.'
max_dist