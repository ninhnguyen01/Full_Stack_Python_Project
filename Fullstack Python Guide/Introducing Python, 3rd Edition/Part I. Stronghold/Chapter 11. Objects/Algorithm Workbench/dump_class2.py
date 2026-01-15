# Call print(hydrogen). In the definition of Element, change the name of the method dump() to __str__, create a new hydrogen object, and call print(hydrogen) again.
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return self.name, self.symbol, self.number
    
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)
