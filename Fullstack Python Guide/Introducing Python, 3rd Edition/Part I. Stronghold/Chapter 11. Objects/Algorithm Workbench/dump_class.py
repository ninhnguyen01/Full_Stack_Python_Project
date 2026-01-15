# For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        return self.name, self.symbol, self.number
    
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.dump())
