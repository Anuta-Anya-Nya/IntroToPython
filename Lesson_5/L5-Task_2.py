# создать список заданной длины из рандоиных чисел, взять каждыц элемент и прописать возрастающие последовательности в списке со списками
from array import array
from codecs import replace_errors
from itertools import starmap
from pkgutil import iter_importers
from random import randint
from re import I


def create_list(num: int):
    return [randint(0, num*2) for i in range(0, num)]


def create_posledov(arr):
    new_list = []
    for i in range(len(array)):
        value = array[i]
        arr_value = [value]
        for j in range(i+1, len(array)):
            if array[j] > value:
                arr_value.append(array[j])
                value = array[j]
        if len(arr_value) > 1:
            new_list.append(arr_value)
    return new_list


array = create_list(10)
print(array)
print(create_posledov(array))


# 1. sample, replace
# 2. iter_importers - кодирование growby, starmap, проверить наичие файлов import pass, exist
# 3. shr(эмодзи в десятичном)
