# Kilometer converter to Mile  

distance = float(input('Enter distance in kilometer: '))

def distance_convert():
    conversion = 0.6214
    miles = distance * conversion    
    print(f'{miles:.1f}')

distance_convert()