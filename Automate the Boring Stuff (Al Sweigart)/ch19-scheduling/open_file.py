import subprocess

file = open('ch19-scheduling/text/hello.txt', 'w')
file.write('Hello world!')
file.close()

subprocess.run(['open', 'ch19-scheduling/text/hello.txt'])