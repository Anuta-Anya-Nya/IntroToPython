import cheking_values as chek
import sys


def start_menu():
    print("Выберите действие:\n\
        1 - записать контакт\n\
        2 - найти контакт\n\
        3 - конвертировать файл\n\
        q - выход")
    value = input("Введите значение: ")
    while not chek.cheking_menu(value):
        value = input("Введено неверное значение! Повторите ввод: ")
    if value == "q":
        sys.exit()
    return int(value)


def info_contact():
    s = input("Введите фамилию: ")
    n = input("Введите имя: ")
    tel = input("Введите телефон: ")
    while not chek.cheking_tel(tel):
        tel = input("Неверный ввод! Введите цифры: ")
    text = input("Введите описание: ")
    file_name = input("Введите имя файла для записи контакта: ")
    while not chek.format_file(file_name):
        file_name = input("Неверный формат файла, повторите ввод: ")
    return s, n, tel, text, file_name


def info_for_find():
    file_name = input("Введите имя файла в котором будет поиск фамилии: ")
    while not chek.format_file(file_name):
        file_name = input("Неверный формат файла, повторите ввод: ")
    s = input("Введите фамилию для поиска: ")
    return file_name, s


def info_for_convert():
    file_name = input("Введите имя файла который необходимо конвертировать: ")
    while not chek.format_file(file_name):
        file_name = input("Неверный формат файла, посторите ввод: ")
    form = input("Введите формат для конвертации (txt или csv): ")
    while not chek.format_file_conv(form):
        form = input("Неверный формат файла, посторите ввод: ")

    return file_name, form
