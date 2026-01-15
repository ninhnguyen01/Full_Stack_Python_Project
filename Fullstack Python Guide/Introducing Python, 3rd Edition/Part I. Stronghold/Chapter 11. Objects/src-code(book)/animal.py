class Animal:
     def says(self):
            return 'I speak!'

class Horse(Animal):
     def says(self):
         return 'Neigh!'

class Donkey(Animal):
     def says(self):
         return 'Hee-haw!'

class Mule(Donkey, Horse):
     pass

class Hinny(Horse, Donkey):
     pass

mule = Mule()
hinny = Hinny()
mule.says()
hinny.says()

class PrettyMixin():
     def dump(self):
         import pprint
         pprint.pprint(vars(self))

class Thing(PrettyMixin):
     pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()

class Duck:
     def __init__(self, input_name):
         self.name = input_name

fowl = Duck('Daffy')
print(fowl.name)

class Duck():
     def __init__(self, input_name):
         self._hidden_name = input_name
     def get_name(self):
         print('')
         return self._hidden_name
     def set_name(self, input_name):
         print('inside the setter')
         self._hidden_name = input_name

don = Duck('Donald')
don.get_name()

don.set_name('Donna')
don.get_name()

class Duck():
    def __init__(self, input_name):
        self._hidden_name = input_name
    def get_name(self):
        print('')
        return self._hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self._hidden_name = input_name
    name = property(get_name, set_name)

don = Duck('Donald')
don.get_name()
don.set_name('Donna')
don.get_name()

don = Duck('Donald')
print(don.name)
don.name = 'Donna'
print(don.name)

class Duck():
 def __init__(self, input_name):
     self._hidden_name = input_name
 @property
 def name(self):
     print('')
     return self._hidden_name
 @name.setter
 def name(self, input_name):
     print('inside the setter')
     self._hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

class Duck():
 def __init__(self, input_name):
     self.__name = input_name
 @property
 def name(self):
     print('')
     return self.__name
 @name.setter
 def name(self, input_name):
     print('inside the setter')
     self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

print(fowl._Duck__name)
