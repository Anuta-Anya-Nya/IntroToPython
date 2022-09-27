# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27
number = float(input())
length_number = len(str(number))
number = int(number*10**(length_number-2))
sum = 0
while number > 0:
    sum += number % 10
    number = number//10
print(sum)
