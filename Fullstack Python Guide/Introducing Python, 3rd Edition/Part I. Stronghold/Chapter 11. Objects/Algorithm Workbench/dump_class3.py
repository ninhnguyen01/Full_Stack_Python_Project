# Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
class Element():
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number
    def get_name(self):
        def __str__(self):
            super().__init__(self)
        return self._name, self._symbol, self._number
    
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen._name, hydrogen._symbol, hydrogen._number)
