# Вывести числа от -n до n
n = int(input('Number N: '))
if n > 0:
    for i in range(-n, n+1):
        print(i, end=" ")
else:
    for i in range(n, -n+1):
        print(i, end=" ")
