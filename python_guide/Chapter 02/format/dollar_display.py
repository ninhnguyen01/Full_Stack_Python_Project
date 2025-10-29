# This program demonstrates how a floating-point
# number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $ ',\
      format(annual_pay, ',.2f'), \
      sep='')

# convert to other currency
south_korean_won = 1434.55 # Oct 29, 4:29 AM UTC  (date of currency value)
dollar_to_won = annual_pay * south_korean_won
print('Your annual pay of $ ',\
      format(annual_pay, ',.2f'),\
                   ' = ₩ ',format(dollar_to_won, ',.2f'),\
                        sep='')