from dataclasses import dataclass

@dataclass
class Unit:
    abbrev: str
    value_in_std_units: float

gram = Unit(abbrev="g", value_in_std_units=0.001)
print(gram.abbrev) # Prints 'g'
