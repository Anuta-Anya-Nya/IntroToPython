# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
from random import randint


def create_list(n):
    lst = [randint(1, n*3) for i in range(n)]
    print(lst)
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]

# return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


print(create_list(9))
