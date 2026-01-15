from dataclasses import dataclass
@dataclass
class TeenyDataClass:
     name: str

teeny = TeenyDataClass('bitsy')
print(teeny.name)

@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 46)
print(snowman)

duck = AnimalClass(habitat='lake', name='duck')
print(duck)

AnimalClass(name='yeti', habitat='Himalayas', teeth=46)
AnimalClass(name='duck', habitat='lake', teeth=0)
