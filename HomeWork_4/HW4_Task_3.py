# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности в том же порядке.
from random import choices


def create_list(num: int):
    if num <= 1:
        print("Negative value of the number of numbers!")
        return []
    else:
        numbers_list = choices(range(0, num-num//3), k=num)
        return numbers_list
        # for i in range(count)
        # number_list.append(randrange(count))


def find_uniq(array):
    if not array:
        print("Negative value of the number of numbers!")
        return array
    else:
        new_array = []
        # делаем словарь из массива, ключи числа, значения - 0
        d = dict.fromkeys(array)  # d={}.fromkeys(array, 0) 0 - значение
        # for k in d.keys():
        #     count = 0
        #     for i in array:
        #         if k == i:
        #             count += 1
        #     if count == 1:
        #         new_array.append(k)
        for i in array:
            d[i] += 1
        for k in d:
            if d[k] == 1:
                new_array.append(k)
        return new_array


some_array = create_list(10)
print(some_array)
print(find_uniq(some_array))
