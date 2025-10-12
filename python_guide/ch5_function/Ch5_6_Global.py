# Global Variables and Global Constants

# Create a Global Variable.
my_value = 10

def show_value():
    print(my_value)

show_value()

# Creat a Global Variable.
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

main() 

""" Global Constants """
# The following is used as a global constant to represent 
# the contribution rate.

CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Contribution for gross pay ${contrib:,.2f}.')
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f'Contribution for bonuses ${contrib:,.2f}.')

main()
