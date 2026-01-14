# Define a generator function called get_odds() that returns the odd numbers from range(10). Use a 'for loop' to find and print the third value returned.
def get_odds():
    for od in range(10):
        if od % 2 != 0:
            print(od)

def third_value():
      for od in range(10):
        if od != 5:
            continue
        else:
            print(od)
            break

get_odds()
print()
third_value()
