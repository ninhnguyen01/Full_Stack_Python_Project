# Bug Collector Program
import sys

MAX = 10
total_bugs = 0

for b in range(MAX):
    day_bugs = int(input('Enter the number of bugs (Max entry: 10) discovered today ("0" to exit): '))
    total_bugs += day_bugs
    with open('bug_track_program/txt/bug_count.txt','w') as f:
        f.writelines("Bug Count: " + str(total_bugs))
        f.close()
        if day_bugs != 0:
            print("Bug count collected!")

        elif day_bugs == 0:
            print("Program ended!")
            sys.exit()
    