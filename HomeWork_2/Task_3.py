# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
n = int(input())
list_number = []
sum = 0
for i in range(1, n+1):
    result = round((1+1/i)**i)
    list_number.append(result)
    sum += result
print(list_number, sum)
