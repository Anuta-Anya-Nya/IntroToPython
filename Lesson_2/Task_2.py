# Создать список длины n где элементы 3к+1, где к от 1 до n включительно
n = int(input())
numbers_list = []
for i in range(1, n+1):
    numbers_list.append(3 * i+1)
print(numbers_list)
