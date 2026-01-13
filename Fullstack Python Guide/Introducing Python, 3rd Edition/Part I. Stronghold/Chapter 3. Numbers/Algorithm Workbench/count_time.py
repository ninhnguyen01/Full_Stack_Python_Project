# How many seconds are in an hour? Create a program as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).

seconds = 60
hour = input('Enter number of hours: ') # 1 hour is 60 minutes
minutes = input('Enter number of minutes: ') # 1 minute is 60 seconds 

hour_result = int(hour) * 60
seconds_result = seconds * int(minutes)
print(f'{hour} hour(s) = {hour_result} minute(s)\n{minutes} minute(s) = {seconds_result} second(s)')
print()

# Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
seconds_per_hour = hour_result * seconds
print(f'{hour} hour(s) : {seconds_per_hour} second(s)')
print()

# How many seconds are in a day? Use your seconds_per_hour variable.
if hour == '24':
    print(f'24 hours in 1 day is {seconds_per_hour} second(s)')
    print()

# Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.
if hour == '24':
    seconds_per_day = seconds_per_hour
    print(f'Seconds per day is {seconds_per_day} second(s)')
    print()

# Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
if hour == '24':
    seconds_per_hour = 3600
    seconds_per_day = 86400
    result = seconds_per_day / seconds_per_hour 
    print(f'{seconds_per_day} seconds is {result} hours')
    print()

# Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?    
if hour == '24':
    seconds_per_hour = 3600
    seconds_per_day = 86400
    result = seconds_per_day // seconds_per_hour 
    print(f'{seconds_per_day} seconds is {result} hours')
    print()
    