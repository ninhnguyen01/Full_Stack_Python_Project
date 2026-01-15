class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))

# But the string eh will not match ha:
print(first.equals(third))

class Word():
     def __init__(self, text):
         self.text = text
     def __eq__(self, word2):
         return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)

class Word():
     def __init__(self, text):
         self.text = text
     def __eq__(self, word2):
         return self.text.lower() == word2.text.lower()
     def __str__(self):
         return self.text
     def __repr__(self):
         return 'Word("'  + self.text  + '")'

first = Word('ha')
print(first)          # uses __repr__
Word("ha")
print(first)   # uses __str__

class Bill():
     def __init__(self, description):
         self.description = description

class Tail():
     def __init__(self, length):
         self.length = length

class Duck():
     def __init__(self, bill, tail):
         self.bill = bill
         self.tail = tail
     def about(self):
         print('This duck has a', self.bill.description,
             'bill and a', self.tail.length, 'tail')

a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()
