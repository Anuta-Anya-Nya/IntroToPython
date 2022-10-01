# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
# Напишите программу, определяющую присутствует ли в заданном списке число, полученное от пользователя

from random import sample  # sample возвращает набор в виде списка


def find_number(num_length=0, number=0):
    num_length = num_length if num_length > 0 else -num_length
    # берет цифры из последовательности range(1, num*2) и второй параметр сколько чисел возьмет и перемешает
    some_list = sample(range(1, num_length*2), num_length)
    print(some_list)
    if number in some_list:
        return True
    return False


list_numbers = int(input("Задайте длину списка: "))
num_polz = int(input("Задайте число для поиска: "))
print(find_number(list_numbers, num_polz))
