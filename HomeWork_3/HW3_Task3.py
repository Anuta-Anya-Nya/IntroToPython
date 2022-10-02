# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
def convert_to_2(number):
    some_list = []
    while number > 0:
        some_list.insert(0, number % 2)
        number = number//2
    print(''.join(map(str, some_list)))


# подумать над отрицательными числами и 0. может рекурсию??
convert_to_2(int(input()))
