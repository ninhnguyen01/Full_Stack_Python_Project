# Property Tax Program
actual_val = float(input("Enter the property's actual value: "))

def property_val():
    assess_val = actual_val * 60 / 100
    property_tax = (assess_val / 100) * 0.72
    print(assess_val)
    print(f'{property_tax:.2f}')

property_val()