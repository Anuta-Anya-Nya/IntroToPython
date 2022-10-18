from datetime import datetime as dt
math_oper = {
    1: "+",
    2: "-",
    3: "*",
    4: "/",
    5: "**",
    6: "** 0.5",
    7: "//",
    8: "%"
}


def calc_log(a, b, oper, res):
    day_time = dt.now().strftime('%d-%m-%Y %H:%M')
    with open('log.txt', 'a', encoding="utf-8") as file:
        if oper == 6:
            file.write(
                f'{day_time} Выражение: {a} {math_oper[oper]} = {res}\n')
        else:
            file.write(
                f'{day_time} Выражение: {a} {math_oper[oper]} {b} = {res}\n')


def div_zero_log(a, b):
    day_time = dt.now().strftime('%d-%m-%Y %H:%M')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write(f'{day_time} Ошибка!: {a} невозможно поделить на {b}!\n')


def sqrt_negat_log(a):
    day_time = dt.now().strftime('%d-%m-%Y %H:%M')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write(
            f'{day_time} Ошибка!: Невозможно найти квадратный корень числа {a}!\n')
