# Boolean Variables

# A bool data type allows you to create variables that may reference one
# of two possible values: True or False.

sales = 51000 # Enter a value for sales

if sales >= 50000:
    sales_quota_met = True
else:
    sales_quota_met = False


if sales_quota_met:
    print('You have met your sales quota!')

if sales_quota_met == True:                     # Equivalent Code
    print('You have met your sales quota!')
