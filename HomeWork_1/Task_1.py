# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number = int(input("Number: "))
if number == 6 or number == 7:
    print('Weekend')
elif number > 0 and number <= 5:
    print('Workday')
else:
    print('It is not a day of the week!')
