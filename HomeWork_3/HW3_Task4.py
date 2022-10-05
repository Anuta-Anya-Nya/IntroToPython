# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform


def find_minim_maxim(number):
    if number > 1:  # если в списке 1 элемент, найти min и max невозможно
        numbers_list = []
        new_list = []
        for i in range(number):
            num = round(uniform(1, 10), 2)
            numbers_list.append(num)
            # num%1 отбивает целую часть
            new_list.append(round(num-int(num), 2))
        print(numbers_list)
        print(round(max(new_list)-min(new_list), 2))
    else:
        print("Error!")


find_minim_maxim(int(input()))
