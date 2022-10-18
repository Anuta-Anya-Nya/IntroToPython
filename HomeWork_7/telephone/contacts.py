import user as us
from os import path


def write_contact():
    tpl = us.info_contact()
    with open(tpl[4], 'a', encoding="utf-8") as file:
        if tpl[4][-3:] == "txt":
            file.write(" ".join(tpl[:4])+"\n")
        else:
            file.write(";".join(tpl[:4])+"\n")


def find_contact():
    file_name, surname = us.info_for_find()
    if path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                if file_name[-3:] == "txt":
                    if line.split()[0].lower() == surname.lower():
                        print("Найдено: " + line)
                else:
                    if line.split(';')[0].lower() == surname.lower():
                        print("Найдено: " + line)

    else:
        print("Файл отсутствует")
