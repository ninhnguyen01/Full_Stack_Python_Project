while True:
    value = input("Enter Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0: # an even number
        continue
    print(number, "squared is", number*number)