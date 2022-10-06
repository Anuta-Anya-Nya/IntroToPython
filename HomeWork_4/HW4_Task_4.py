# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
from random import choices
import math


def create_list(num):
    if num < 1:
        print("Negative value of the number of numbers!")
        return []
    else:
        # для массива коэффициентов длина должна быть на 1 больше коэффициента
        numbers_list = choices(range(-10, 11), k=num+1)
        return numbers_list


def write_polynom(num_list):
    with open('result.txt', 'a', encoding="utf-8") as my_f:
        if not num_list:
            my_f.write("Коэффициент введен неверно!\n")
        else:
            for i in range(0, len(num_list)):
                if num_list[i] > 0 and i == 0:  # для первого положительного члена
                    my_f.write(f"{num_list[i]}")
                elif num_list[i] > 0:
                    my_f.write(f"+ {num_list[i]}")
                elif num_list[i] < 0:
                    my_f.write(f"- {abs(num_list[i])}")
                if i < len(num_list)-1 and num_list[i] != 0:
                    my_f.write(f"*x^{len(num_list)-1-i} ")
            my_f.write(" = 0 \n")


for i in range(3):
    numbers = create_list(int(input("k: ")))
    print(numbers)
    write_polynom(numbers)
