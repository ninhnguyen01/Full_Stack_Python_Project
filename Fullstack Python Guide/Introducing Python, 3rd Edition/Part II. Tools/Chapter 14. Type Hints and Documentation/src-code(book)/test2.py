def int_to_str(num: int) -> str:
    return str(num)

def str_to_int(txt: str) -> int:
    return int(txt)

txt = int_to_str(19)
txt = int_to_str(47) # error with 47.5 (float)
txt = int_to_str(0) # error with "" (str)

num = str_to_int("56")
num = str_to_int("")
num = str_to_int('98') # error with 98 (int)
