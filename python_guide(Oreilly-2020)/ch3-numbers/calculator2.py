# calculator program
hour = 1.0
min =  1
sec = 60

# multiply 60 seconds in a min with 60 minute in an hour
print("Result: " + str(((min * 60) * sec)) + " seconds in 1 hour")

# calculate total seconds in a day
seconds_per_hour = 3600
hours_in_day = 24
print("Result:" , hours_in_day * seconds_per_hour, "seconds in a day")

# calculate hours in a day
seconds_per_day = 86400
print("Result:" , float(seconds_per_day / seconds_per_hour), "hours in a day")

# calculate hours in a day
seconds_per_day = 86400
print("Result:" , int(seconds_per_day / seconds_per_hour), "hours in a day")