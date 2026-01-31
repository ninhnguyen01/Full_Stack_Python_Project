import profile

def func():
    num = 5
    num *= 2
    print(f"{num =}")

profile.run("func()")
