from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)

Duck(bill='wide orange', tail='long')
print(duck.bill)
print(duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

Duck(bill='wide orange', tail='long')
duck2 = Duck(bill = 'wide orange', tail = 'long')

# Named tuples are immutable, but you can replace one or more fields and return another named tuple:
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

Duck(bill='crushing', tail='magnificent')

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)

# You can add fields to a dictionary:
duck_dict['color'] = 'green'
print(duck_dict)
