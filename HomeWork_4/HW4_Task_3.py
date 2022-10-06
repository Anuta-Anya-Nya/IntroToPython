# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности в том же порядке.
from random import choices


def create_list(num):
    if num <= 1:
        print("Negative value of the number of numbers!")
        return []
    else:
        numbers_list = choices(range(0, num-num//3), k=num)
        return numbers_list


def find_uniq(array):
    if not array:
        print("Negative value of the number of numbers!")
        return array
    else:
        new_array = []
        d = dict.fromkeys(array)
        for k in d.keys():
            count = 0
            for i in array:
                if k == i:
                    count += 1
            if count == 1:
                new_array.append(k)
        return new_array


some_array = create_list(10)
print(some_array)
print(find_uniq(some_array))
