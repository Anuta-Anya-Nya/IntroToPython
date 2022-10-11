# Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
def match_poly():
    list_poly = []
    list_poly_2 = []
    with open('poly.txt', 'r', encoding="utf-8") as my_f:
        for line in my_f:  # цикл для пробежки по строчкам
            list_poly.append(line)
    # my_f.close()  # разрыв связи
    with open('poly_2.txt', 'r', encoding="utf-8") as my_f_2:
        for line in my_f_2:
            list_poly_2.append(line)
    # my_f_2.close() закрывать не надо, менеджер контекста закрывается автоматически
    with open('res.txt', 'a', encoding="utf-8") as my_f_res:
        if not len(list_poly) == len(list_poly_2):
            my_f_res.write("The contents of the files do not match!\n")
        else:
            for i in range(0, len(list_poly)):
                if (list_poly_2[i][0]) == "-":
                    my_f_res.write(f"{list_poly[i][0:-5]}{list_poly_2[i]}")
                else:
                    my_f_res.write(f"{list_poly[i][0:-5]}+ {list_poly_2[i]}")
            my_f_res.write("\n")


match_poly()


# def poly_sum(name_1: str, name_2: str):  # слеш переносит одну строку на строку ниже
#     with open(name_1, 'r', encoding="utf-8") as my_f_1, \
#             open(name_2, 'r', encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()  # считываем все строки из файла
#         second = my_f_2.readlines()

#         if len(first) == len(second):
#             with open('sum_poly.txt', "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):  # кортеж индекс-значение
#                     my_f_3.write(f"{v[-5]} + {second[i]}")
#         else:
#             print("error!")
