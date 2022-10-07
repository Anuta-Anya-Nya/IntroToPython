# Задайте 2 числа, найдите наименьшее общее кратное этих двух чисел
import math


a = int(input())
b = int(input())
print(a*b//math.gcd(a, b))
