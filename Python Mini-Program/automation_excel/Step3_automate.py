""" This is the final file. The Execution file. """
""" You can run the entire program in this single file after editing all the previous files. """
import subprocess

# Import package for automation
# Specify the name of the Python files within the file path
file_path = ['automation_excel/Step1_read_data.py','automation_excel/Step2_graph.py']

# A loop that read through all the files
for files in file_path:
    subprocess.run(['python3', files], check=True)
    # Confirmaton of program run
    print('AUTOMATION PROGRAM EXECUTED')
