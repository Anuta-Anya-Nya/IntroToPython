# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input('coordinate x: '))
y = int(input('coordinate y: '))
if x == 0 and y == 0:
    print('Error!')
elif x > 0 and y > 0:
    print('quarter 1')
elif x > 0 and y < 0:
    print('quarter 4')
elif x < 0 and y < 0:
    print('quarter 3')
elif x < 0 and y > 0:
    print('quarter 2')
elif x == 0:
    print('axis Y')
else:
    print('axis X')
