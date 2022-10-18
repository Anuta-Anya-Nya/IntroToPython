math_operations = {
    1: lambda x, y: x+y,
    2: lambda x, y: x-y,
    3: lambda x, y: x*y,
    4: lambda x, y: x/y,
    5: lambda x, y: x**y,
    6: lambda x, y: x**0.5,
    7: lambda x, y: x//y,
    8: lambda x, y: x % y
}


def calc(numb_oper, a, b):
    return math_operations[numb_oper](a, b)


#print(calc(8, 3, 2))
# def sum_numb():
#     return x + y


# def sub_numb():
#     return x - y


# def mult_numb():
#     return x * y


# def div_numb():
#     return x + y


# def pow_numb():
#     return x ** y


# def sqrt_numb():
#     return x ** 0.5


# def div_2_numb():
#     return x // y


# def r_div_numb():
#     return x % y
