import cheсking_values as cheсk
import sys
from os import path


def ask_file_name():
    file_name = input("Введите имя файла базы данных для работы (csv/txt): ")
    while not cheсk.format_file(file_name):
        file_name = input("Неверный формат файла, повторите ввод: ")
    if path.exists(file_name):
        return file_name
    else:
        print("Файл отсутствует")
        sys.exit()


def start_menu():
    print("Выберите действие:\n\
    1 - просмотреть все записи\n\
    2 - создать новую запись\n\
    3 - найти запись\n\
    4 - изменить запись\n\
    5 - удалить запись\n\
    6 - конвертировать файл базы данных\n\
    q - выход")
    while True:
        value = input("Введите значение: ")
        if cheсk.cheсking_menu(value):
            break
        print("Введено неверное значение!")
    if value == "q":
        sys.exit()
    return int(value)


def menu_write():
    s = input("Введите фамилию: ")
    n = input("Введите имя: ")
    p = input("Введите отчество: ")
    tel = input("Введите телефон: ")
    while not cheсk.cheсking_number(tel):
        tel = input("Неверный ввод! Введите цифры: ")
    while True:
        gender = input("Введите пол (муж/жен): ")
        if cheсk.checking_gender(gender):
            break
        print("Введено неверное значение, повторите ввод!")
    pos = input("Введите должность: ")
    salary = input("Введите зарплату: ")
    while not cheсk.cheсking_number(salary):
        salary = input("Неверный ввод! Введите цифры: ")

    return s, n, p, tel, gender, pos, salary


def menu_for_find():
    print("Выберите поле для поиска:\n\
        1 - id\n\
        2 - фамилия\n\
        3 - имя\n\
        4 - отчество\n\
        5 - телефон\n\
        6 - пол\n\
        7 - должность\n\
        8 - зарплата\n\
        q - выход")
    value = input("Введите значение: ")
    while not cheсk.cheсking_menu_find(value):
        value = input("Введено неверное значение! Повторите ввод: ")
    if value == "q":
        sys.exit()
    s = input("Введите значение для поиска: ")
    return int(value), s


def print_find(lst):
    if not len(lst):
        print("Сотрудников не найдено")
    else:
        print(f"Найдено сотрудников: {len(lst)}\n {lst}")


def info_for_convert():
    file_name = input("Введите имя файла который необходимо конвертировать: ")
    while not cheсk.format_file(file_name):
        file_name = input("Неверный формат файла, повторите ввод: ")
    form = input("Введите формат для конвертации (txt или csv): ")
    while not cheсk.format_file_conv(form):
        form = input("Неверный формат файла, посторите ввод: ")

    return file_name, form


def menu_for_edit():
    print("Выберите поле для изменения:\n\
        1 - фамилия\n\
        2 - имя\n\
        3 - отчество\n\
        4 - телефон\n\
        5 - пол\n\
        6 - должность\n\
        7 - зарплата\n\
        q - выход")
    while True:
        value = input("Введите значение: ")
        if cheсk.cheсking_menu_edit(value):
            break
        print("Введено неверное значение!")
    if value == "q":
        sys.exit()
    while True:
        id = input("Введите значение id для поиска сотрудника: ")
        if cheсk.cheсking_number(id):
            break
        print("Введено неверное значение!")
    text = input("Введите новое значение поля: ")
    if value == "4" or value == "7" and not text.isdigit():
        while not text.isdigit():
            text = input("Введено неверное значение поля, введите цифры: ")
    return int(value), id, text


def menu_for_del():
    print("Строку с каким id вы хотите удалить?")
    while True:
        id = input("Введите значение id или q для выхода из программы: ")
        if cheсk.cheсking_number(id):
            break
        print("Введено неверное значение!")
    if id == "q":
        sys.exit()
    return id


def menu2_for_del():
    while True:
        value = input(
            "Вы уверены, что хотите удалить строку (1 - да, 2 - нет): ")
        if cheсk.cheсking_number(value) and (value == "1" or value == "2"):
            break
        print("Введено неверное значение!")
    return int(value)
