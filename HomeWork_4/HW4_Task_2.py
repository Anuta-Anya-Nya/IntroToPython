# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

def find_prime_factors(num):
    list_prime_factors = []
    while num > 1:
        for i in range(2, num+1):
            if not num % i:
                if i == 2:
                    list_prime_factors.append(i)
                    num = num // i  # num //=i
                    break
                else:
                    for k in range(2, i):
                        count = 0
                        if not i % k:
                            count += 1
                    if not count:
                        list_prime_factors.append(i)
                        num = num // i
                        break
    return list_prime_factors


print(find_prime_factors(9990))
