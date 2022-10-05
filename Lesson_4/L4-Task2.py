# Найдите корни квадратного уравнения ax2+bx+c=0 с помощью модуля.
# запросите значение a, b, c 3 раза. Уравнения и корни запишите в файл
from math import sqrt


def find_roots(a, b, c):
    d = b ** 2 - 4*a*c
    with open('result.txt', 'a', encoding="utf-8") as my_f:
        my_f.write(f"{a}x^2 + {b}x + {c} = 0\n")
        if d > 0 and a:  # чтобы "a" не был равен нулю
            # в файлы пишутся ТОЛЬКО строки
            my_f.write(str((-b+sqrt(d)) / (2 * a)) + "\n")
            my_f.write(str((-b-sqrt(d)) / (2 * a)) + "\n")
        elif d == 0 and b:
            my_f.write(str(-b / (2 * a)) + "\n")
        else:
            my_f.write("Корней нет\n")


for i in range(3):
    find_roots(int(input("a: ")), int(input("b: ")), int(input("c: ")))
