# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]
number = int(input())
if number < 1:
    print("Error!")
else:
    some_list = [1]
    result_number = 1
    for i in range(2, number+1):
        result_number *= i
        some_list.append(result_number)
    print(some_list)
