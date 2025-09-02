def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def power(base, pow):
    return base**pow


def square(base):
    return base**2


def greet(이름="낯선자", 나이=20):
    ret_str = ""
    if 나이 >= 50:
        ret_str += "안녕하십니까 "
    elif 나이 >= 20:
        ret_str += "안녕하신가 "
    else:
        ret_str += "안녕 "
    ret_str += f"{이름}!"
    return ret_str

