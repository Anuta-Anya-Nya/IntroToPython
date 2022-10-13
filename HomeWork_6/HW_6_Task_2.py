# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
def find_numb(n):
    lst = [i for i in range(20, n+1) if not i % 20 or not i % 21]
    return lst


print(find_numb(100))
