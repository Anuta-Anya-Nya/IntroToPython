# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
number = int(input())
list_numbers = []
for i in range(number):
    list_numbers.append(i)
print(list_numbers)
for i in list_numbers:
    index_random = random.randint(0, len(list_numbers)-1)
    temp = list_numbers[i]
    list_numbers[i] = list_numbers[index_random]
    list_numbers[index_random] = temp
print(list_numbers)
