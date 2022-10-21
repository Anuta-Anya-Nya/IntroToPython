import user as us
from os import path


def convert_file():
    file_name, form = us.info_for_convert()
    if path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file, \
                open(f"{file_name[:-4]}.{form}", 'w', encoding="utf-8") as r_file:
            if form == file_name[-3:]:
                print("Нельзя конвертировать в исходный формат!")
            else:
                for line in file:
                    if form == "txt" and file_name[-3:] == "csv":
                        r_file.write(' '.join(line.strip().split(';'))+"\n")
                    else:
                        r_file.write(';'.join(line.strip().split()) + "\n")
                print("Готово!")
    else:
        print("Файл для конвертации отсутствует")
