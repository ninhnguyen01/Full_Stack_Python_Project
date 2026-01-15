# Make a class called Element, with instance attributes name, symbol, and number. Create an object of this class with the values Hydrogen, H, and 1.
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

water = Element('Hydrogen', 'H', 1)
print(water.name, water.symbol, water.number)
