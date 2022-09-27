# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
first_pos = int(input())
second_pos = int(input())
number = int(input())
list_numbers = []
list_length = number*2+1
if first_pos < 1 or second_pos < 1 or first_pos > list_length or second_pos > list_length:
    print('Error!')
else:
    for i in range(-number, number+1):
        list_numbers.append(i)
    print(list_numbers)
    print(list_numbers[first_pos-1]*list_numbers[second_pos-1])
