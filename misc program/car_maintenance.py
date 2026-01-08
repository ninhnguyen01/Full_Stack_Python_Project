# Automobile costs 

car_loan = float(input('Enter loan cost (monthly): '))
car_insurance = float(input('Enter insurance cost (monthly): '))
car_gas = float(input('Enter gas cost (monthly): '))
 
def cost():
    monthly_auto_cost = car_loan + car_insurance + car_gas 
    annual_cost = monthly_auto_cost * 12
    total = f' Monthly: {monthly_auto_cost}. Annual: {annual_cost}'
    print(total)

cost()
