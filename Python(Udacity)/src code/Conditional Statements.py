points = 174  # use this input to make your submission


if points >= 1 and points <= 50:
    Prize = 'no prize'
    print("Oh dear, no prize this time.")
elif points >=51 and points <= 150:
    Prize = 'wooden rabbit'
    print("Congratulations! You won a {}!".format(Prize))
elif points >=151 and points <= 180:
    Prize = 'wafer-thin mint'
    print("Congratulations! You won a {}!".format(Prize))
elif points >=181 and points <= 200:
    Prize = 'penguin'
    print("Congratulations! You won a {}!".format(Prize))
