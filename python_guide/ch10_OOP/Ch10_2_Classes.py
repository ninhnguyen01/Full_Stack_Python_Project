# Classes

""" Class Definiton """

import random
class Coin:
    def __init__(self):
        self.sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup
        
def main():
    my_coin = Coin()
    print('This side is up:',my_coin.get_sideup())
    print('I am tossing the coin...')
    my_coin.toss()
    print('This side is up:',my_coin.get_sideup())

if __name__ == '__main__':
    main()

""" Hiding Attributes """
import random
class Coin:
    def __init__(self):
        self.sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print('This side is up:',my_coin.get_sideup())
    print('I am tossing the coin...')
    my_coin.toss()
    my_coin.sideup = 'Heads'
    print('This side is up:',my_coin.get_sideup())

if __name__ == '__main__':
    main()

# coindemo3
import random
class Coin:
    def __init__(self):
        self.__sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    def get_sideup(self):
        return self.__sideup

def main():
    my_coin = Coin()
    print('This side is up:',my_coin.get_sideup())
    print('I am going to toss the coin ten times:')
    for count in range (10):
        my_coin.toss()
        print(my_coin.get_sideup())

if __name__ == '__main__':
    main()

""" Storing Classes in Modules """

# check coin.py 
# check coin_demo4.py 


""" The BankAccount Class """

# check bankaccount.py
# check account_test.py

# The __str__ Method (section)
# check bankaccount2.py
# check account_test2.py

