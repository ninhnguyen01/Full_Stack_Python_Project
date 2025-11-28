import random
import time

class CoinFlips:     
    def __init__(self, number_of_flips):         
        self.number_of_flips = number_of_flips  # Store the total number of flips         
        self.counter = 0      
    def __iter__(self):         
        return self  # Return a reference of the iterator      
    # Flip the next coin, return the output     
    def __next__(self): 
        if self.counter < self.number_of_flips:             
            self.counter += 1             
            return random.choice(["H", "T"]) 
        else: # Otherwise, stop execution with StopIteration
            raise StopIteration
    
print()
coin_toss = CoinFlips(int(input("Enter # of toss: ")))
for flip in coin_toss:
    time.sleep(1)
    print(flip) # Pull the next element of three_flips  
print()
print("Toss ended!")
print()
    
         
