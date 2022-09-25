# ПРинимает 2 числа и проверяет являются ли одно квадратом другого

a = int(input("Число а: "))
b = int(input("Число b: "))
if a**2 == b or b**2 == a:
    print("yes")
else:
    print("no")
