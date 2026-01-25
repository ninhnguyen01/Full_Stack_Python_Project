# Write the current date as a string to the text file today.txt.
import datetime as dt

curr_time = dt.datetime.today()
print(curr_time)

with open('Chapter 19. Dates and Times/Algorithm Workbench/today.txt','a') as f:
    f.write('\n')
    f.write(str(curr_time))
    f.close()
