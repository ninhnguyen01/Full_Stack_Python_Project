# Define a decorator called test that prints start when a function is called, and end when it finishes.
def test(func):
   def new_function(*args, **kwargs):
       result = func(*args, **kwargs)
       return result * result
   return new_function

@test
def sum(a, b):
    # return the value of 2 numbers before squaring it from 'test'
    return a + b 

print(sum(3, 4)) 
