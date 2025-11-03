import time, subprocess

minutes = input("Enter break minute(s): ")
remaining_time = 60 * int(minutes)

while remaining_time > 0:
    print(remaining_time)
    time.sleep(1)
    remaining_time -= 1

# mac version of 'subprocess.run'
subprocess.run(['open', '/System/Applications/Music.app'])
subprocess.run(['open', '../ch19-scheduling/music/StereoLove.mp3'])