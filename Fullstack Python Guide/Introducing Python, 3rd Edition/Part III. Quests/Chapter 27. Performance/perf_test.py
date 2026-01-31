import cProfile

def func():
    num = 5
    num *= 2
    print(f"{num =}")

cProfile.run("func()")
