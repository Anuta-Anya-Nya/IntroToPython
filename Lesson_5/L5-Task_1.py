# В списке находится n натуральных чисел, записанных через пробелю
# Среди чисел не хватает одного, чтобы выполнялось условие A[i]-1 = A[i-1].Найдите его
from random import choice


def create_list(numb: int):
    my_list = [i for i in range(0, numb+1)]
    my_list.remove(choice(my_list))
    return my_list


def find_elem(arr):
    if arr[0]:
        return 0
    for i in range(1, len(arr)):
        if (arr[i]-1) != arr[i-1]:
            return arr[i]-1
    return -1


my_list = create_list(9)
print(my_list)
print(find_elem(my_list))
