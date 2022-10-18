import excep as ex
import sys


def choose_format():
    print("Выберите формат числа:\n1 - рациональное \n2 - комплексное \nq - выход")
    value = input("Введите значение: ")
    while not ex.choose_format_ex(value):
        value = input("Введено неверное значение! Повторите еще раз: ")
    if value == "q":
        sys.exit()
    return int(value)


def menu_ration():
    print("Выберите математическую операцию:\n\
    1 - сложение\n\
    2 - вычитание\n\
    3 - умножение\n\
    4 - деление\n\
    5 - возведение в степень\n\
    6 - извлечение квадратного корня\n\
    7 - целочисленное деление\n\
    8 - остаток от деления\n\
    0 - предыдущее меню\n\
    q - выход")
    value = input("Введите значение: ")
    while not ex.menu_ration_ex(value):
        value = input("Введено неверное значение! Повторите еще раз: ")
    if value == "q":
        sys.exit()
    return int(value)


def menu_compl():
    print("Выберите математическую операцию:\n\
    1 - сложение\n\
    2 - вычитание\n\
    3 - умножение\n\
    4 - деление\n\
    5 - возведение в степень\n\
    6 - извлечение квадратного корня\n\
    0 - предыдущее меню\n\
    q - выход")
    value = input("Введите значение: ")
    while not ex.menu_compl_ex(value):
        value = input("Введено неверное значение! Повторите еще раз: ")
    if value == "q":
        sys.exit()
    return int(value)


def enter_value_ration(num):
    number = input(f"Введите число {num}: ")
    while not ex.enter_value_ex(number):
        number = input(f"Введено не число! Введите число {num}: ")
    return eval(number)


def enter_value_compl_d(num):
    number = input(f"Введите действительную часть числа {num}: ")
    while not ex.enter_value_ex(number):
        number = input(
            f"Введено не число! Введите действительную часть числа {num}: ")
    return eval(number)


def enter_value_compl_m(num):
    number = input(f"Введите мнимую часть числа {num}: ")
    while not ex.enter_value_ex(number):
        number = input(f"Введено не число! Введите мнимую часть числа {num}: ")
    return eval(number)


def print_compl_num(num, compl):
    print(f"Введено комплексное число {num}: {compl}")


def print_result(result):
    print(f"Получен результат: {result}")
