import user as us
from os import path


def convert_file():
    file_name, form = us.info_for_convert()
    if path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file, \
                open(f"{file_name[:-4]}.{form}", 'w', encoding="utf-8") as r_file:
            for line in file:
                r_file.write(line)
    else:
        print("Файл для конвертации отсутствует")
