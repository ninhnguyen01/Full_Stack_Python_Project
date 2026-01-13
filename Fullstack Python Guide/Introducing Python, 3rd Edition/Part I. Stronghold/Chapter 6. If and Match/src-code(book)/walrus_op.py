# the walrus operator, which looks like this:
# name := expression
post_limit = 300
post_string = "Blah" * 50
if (diff := post_limit - len(post_string)) >= 0:
     print("A fitting post")
else:
     print("Went over by", abs(diff))
