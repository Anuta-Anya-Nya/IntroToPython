# Проверяет число, кратно ли оно 5 и 10 или 15, но не 30
numb = int(input("Число: "))
if (numb % 5 == 0 and numb % 10 == 0 or numb % 15 == 0) and numb % 30 != 0:
    print('yes')
else:
    print('no')
