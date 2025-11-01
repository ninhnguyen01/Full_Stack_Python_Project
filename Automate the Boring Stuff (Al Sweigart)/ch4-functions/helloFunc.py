def greetings():
    print("Enter your current time (24-hr format): ")
    print("Example: 00-24 (2 digits only)")
    curr_time = int(input())
    if curr_time >= 00 and curr_time <= 11:
        print()
        print(str(curr_time) + ' am')
        print("Good morning!")
    elif curr_time >= 12 and curr_time <= 18:
        print()
        print(str(curr_time) + ' pm')
        print("Good afternoon!")
    elif curr_time > 18 and curr_time < 24:
        print()
        print(str(curr_time) + ' pm')
        print("Good evening!")
    else:
        print("Invalid entry! Wrong format or entry is 24 or above.")

greetings()