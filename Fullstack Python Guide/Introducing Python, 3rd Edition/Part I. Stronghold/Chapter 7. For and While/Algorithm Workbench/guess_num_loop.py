# Assign the value 7 to the variable guess_me, and the value 1 to the variable number. 
# Write a while loop that compares number with guess_me. Print too low if number is less than guess me. 
# If number equals guess_me, print found it! and then exit the loop. If number is greater than guess_me, print oops and then exit the loop. Increment number at the end of the loop.

guess_me  = 7
total_guesses = 0 # accumulator variable
increment_num = 0 # accumulator variable

number = int(input("Enter a number: "))

while number:
    if number < guess_me:
        total_guesses += 1
        increment_num += number
        print("The value is too low!")
        number = int(input("Enter a number: "))

    elif number == guess_me:
        print("Found it!")
        print(f"Total Guesses: {total_guesses}")
        print(f"Total Increment: {increment_num}")
        break

    elif number > guess_me:
        print("Oops! Value is too high!")
        total_guesses += 1
        increment_num += number
        print(f"Total Guesses: {total_guesses}")
        print(f"Total Increment: {increment_num}")
        break
