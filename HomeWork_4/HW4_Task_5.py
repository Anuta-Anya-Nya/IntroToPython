# Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
def match_poly():
    list_poly = []
    list_poly_2 = []
    with open('poly.txt', 'r', encoding="utf-8") as my_f:
        for line in my_f:  # цикл для пробежки по строчкам
            list_poly.append(line)
    my_f.close()  # разрыв связи
    with open('poly_2.txt', 'r', encoding="utf-8") as my_f_2:
        for line in my_f_2:
            list_poly_2.append(line)
    my_f_2.close()
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
