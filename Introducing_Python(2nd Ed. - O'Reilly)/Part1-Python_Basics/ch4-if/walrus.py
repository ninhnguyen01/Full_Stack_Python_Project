# walrus operator
# name:=expression

tweet_limit = 200
tweet_string = "Blah" * 50
if diff:= tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by",  abs(diff))