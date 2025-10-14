# Finding Items in Lists with the 'in' Operator

# 'In' Operator General Format
# item in list

# This program demonstrate the 'in' operator used with a list.
def main():
    prod_nums = ['V475', 'F987', 'Q143', 'R688']
    search = input('Enter a product number: ')
    if search in prod_nums:
        print(f'{search} was FOUND in the list.')
    else:
        print(f'{search} was not found in the list.')

# alternate with 'not in'
    if search not in prod_nums:
        print(f'{search} was NOT found in the list.')
    else:
        print(f'{search} was found in the list.')
        
if __name__ == '__main__':
    main()
