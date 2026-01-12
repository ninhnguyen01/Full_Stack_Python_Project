# 7. A file exists on the disk named students.txt. The file 
# contains several records, and each record contains 2 fields:
# (1) The student's name, and (2) the student's score for the
# final exam.

# Part 1: Create record
num_students = int(input('How many students ' +
    'do you want to add? '))
outputfile = open('Starting Out with Python/ch6-file/algorithm-workbench/students.txt','w')
for count in range(1,num_students+1):
    student_name = input('Enter student name: ')
    student_score_final = float(input('Enter student\'s final exam score: '))
    outputfile.write(f'Name: {student_name}\n')
    outputfile.write(f'Final Exam Score: {student_score_final}\n')
    print()
outputfile.close()

# Part 2: Display Record
infile = open('Starting Out with Python/ch6-file/algorithm-workbench/students.txt','r')
student_name = infile.readline()

while student_name != '':
    student_score_final = infile.readline()
    student_name.rstrip('\n')

    print(f'{student_name}')
    print(f'{student_score_final}')
    print()
    
    student_name = infile.readline()

infile.close()