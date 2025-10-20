#  dynamically executes Python code stored in a string or code object. It is used for evaluating and executing dynamic code.

msg = '''
for i in range(11):
    print(i)
'''

exec(msg)