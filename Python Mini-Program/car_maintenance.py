# 4 Automobile Costs
car_loan = float(input('Enter loan cost: '))
car_insurance = float(input('Enter insurance cost: '))
car_gas = float(input('Enter gas cost: '))
car_oil = float(input('Enter oil cost: '))
car_tire = float(input('Enter tire cost: '))
car_maintenance = float(input('Enter maintenance cost: '))
 
def cost():
    monthly_auto_cost = car_loan + car_insurance + car_gas + car_oil + car_tire + car_maintenance
    print("Monthly Cost: " + str(monthly_auto_cost))
    annual_cost = monthly_auto_cost * 12
    print("Annual Cost: " + str(annual_cost))

cost()