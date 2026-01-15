# Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return berries (Bear), clover (Rabbit), or campers (Octothorpe). Create one object from each and print what it eats.
class Behavior():
    def __init__(self, eat):
        self.eat = eat

class Bear(Behavior):
    def __init__(self, name, eat):
        self.name = name
        super().__init__(eat)
    
class Rabbit(Behavior):
    def __init__(self, name, eat):
        self.name = name
        super().__init__(eat)

class Octothorpe(Behavior):
    def __init__(self, name, eat):
        self.name = name
        super().__init__(eat)


bear = Bear('Bear', 'berries')
print(f'{bear.name} eats {bear.eat}')

rabbit = Rabbit('Rabbit', 'clover')
print(f'{rabbit.name} eats {rabbit.eat}')

octothorpe = Octothorpe('Octothorpe', 'campers')
print(f'{octothorpe.name} eats {octothorpe.eat}')
