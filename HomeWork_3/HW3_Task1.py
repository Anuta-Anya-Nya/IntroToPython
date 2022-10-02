# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(четных индексах).
from random import sample


def find_sum(number):
    if number > 0:
        numbers_list = sample(range(0, number), number)
        print(numbers_list)
        sum = 0
        for i in range(0, number, 2):
            sum += numbers_list[i]
        print(sum)
    else:
        print("Error!")


find_sum(int(input()))
