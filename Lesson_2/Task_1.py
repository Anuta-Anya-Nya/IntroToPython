# получает число n и выдает последовательность 1, -3, 9, -27, 81
number = int(input())
for i in range(number):
    print((-3)**i, end=', ')
print("")

# 2
result = 1
for i in range(number):
    print(result, end=", ")
    result *= (-3)
