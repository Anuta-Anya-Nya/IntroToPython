# Принимает на вход 5 чисел и выводи максимальное
#a = int(input("Число а: "))
#b = int(input("Число b: "))
#c = int(input("Число c: "))
#d = int(input("Число d: "))
#e = int(input("Число e: "))
#list = [a, b, c, d, e]
#max = a
# for i in list:
#    if max < i:
#        max = i
# 1
# print(max)

max = 0
for i in range(5):
    numb = int(input("Число: "))
    if max < numb:
        max = numb
print(max)
