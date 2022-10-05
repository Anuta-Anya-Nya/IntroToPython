# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibon(number):
    if number > 0:
        list_fibon = [0, 1]
        for i in range(0, number-1):
            # формирую правую часть
            list_fibon.append(list_fibon[0+i]+list_fibon[1+i])
        for i in range(1, number*2+1, 2):
            # формирую левую часть без минусов
            list_fibon.insert(0, list_fibon[i]*(-1)**(i-1))
        for i in range(0, number):
            # проставляю минусы в левую часть
            list_fibon[i] *= (-1) ** (i + 1 + number % 2)
        print(list_fibon)
    else:
        print('Error!')


fibon(int(input()))
