def cap(s):

    lines = s.split(". ")

    answer = ""

    for line in lines:

        answer = answer + line[0].upper() + line[1:] + ". "

    return answer[:-2]

s = input("Enter sentence to be capitalized: ")

print(cap(s))