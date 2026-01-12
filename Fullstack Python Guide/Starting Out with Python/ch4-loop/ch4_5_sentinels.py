# Sentinels (Title)

# 4.18 What is a sentinel?
""" A special value that marks the end of a sequence of items. """

# displays property taxes demo
TAX_FACTOR = 0.0065
# Get the first lot number.
print('Enter the property lot number or enter 0 to end.')
lot = int(input('Lot number: '))
# Continue processsing as long as the user does not enter lot number 
# 0.
while lot != 0:
    # Get the property value.
    value = float(input('Enter the property value: '))
    # Calculate the property's tax.
    tax = value * TAX_FACTOR
    # Display the tax.
    print(f'Property tax: ${tax:,.2f}')
    # Get the next lot number.
    print('Enter the next lot number or enter 0 to end.')
    lot = int(input('Lot number: ')) # sentinel 
    # 4.19 Why should you take care to choose a distinctive value as a sentinel?
    """ So that it will not be mistaken as a regular value in the sequence. """
