# Tip, Tax, and Total Program

tip_percentage = 0.18
sales_tax_percentage = 0.07
meal_subtotal = float(input('Enter the total charge for food: '))
meal_tip = meal_subtotal * tip_percentage
meal_salestax= meal_subtotal * sales_tax_percentage
meal_total = meal_subtotal + meal_tip + meal_salestax 
print(meal_total)