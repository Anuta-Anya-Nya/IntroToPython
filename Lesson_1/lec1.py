# print('hello')
# a = 4
# b = 6.4
# c = 'anna'
# print(f'{a} - {b} - {c}')

#original = 23
#inverted = 0
# while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10  # целочисленное деление
# else:
#    print("вот и все")
# print(inverted)

# for i in 1, 2, 3, 4, 5:  # итерируемый объект - набот чисел
#    print(i**2)  # квадрат числа

# list = [1, 2, 3, 4, 5]  # массив называется списком
# for i in list:
#    print(i)

r = range(10)  # объект рэнжей - числа от 0 до 9
for i in r:
    print(i)

for i in 'qwe - ew':  # выведет все символы строка
    print(i)


def f(x):
    if x == 1:
        return 'Целое'  # возвращает строку
    elif x == 2.3:
        return 23  # возвращает число
    else:
        return  # возвращает None


arg = 2
print(f(arg))
print(type(f(arg)))
