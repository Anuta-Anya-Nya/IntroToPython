from tkinter import N


# Вывести первую цифру перед запятой дробного числа
n = float(input('Number: '))
n = n*10 % 10
print(int(n))
