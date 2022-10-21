import user as us
from os import path


def view_card(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def find_id(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        if not len(file.readlines()):
            return 0
        else:
            with open(file_name, 'r', encoding="utf-8") as file:
                last_line = file.readlines()[-1]
                return int(last_line.split(";")[0])


def write_card(file_name, count):
    tpl = us.menu_write()
    with open(file_name, 'a', encoding="utf-8") as file:
        if file_name[-3:] == "csv":
            file.write(f'{str(count+1)};{";".join(tpl)}\n')
        else:
            file.write(f'{str(count+1)};{" ".join(tpl)}\n')
    print("Карта сотрудника добавлена!")


def find_card(file_name):
    where_find, what_find = us.menu_for_find()
    with open(file_name, 'r', encoding="utf-8") as file:
        lst_cards = []
        for line in file:
            if file_name[-3:] == "txt":
                if line.split()[where_find-1].lower().strip() == what_find.lower():
                    lst_cards.append(line.strip())
            else:
                if line.split(';')[where_find-1].lower().strip() == what_find.lower():
                    lst_cards.append(line.strip())
    return lst_cards


def edit_card(file_name):  # для большого файла будет не оптимально?
    pos, id, text = us.menu_for_edit()
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            if file_name[-3:] == "csv":
                line = lines[i].strip().split(';')
                if line[0] == id:
                    line[pos] = text
                    lines[i] = ";".join(line)+"\n"
            else:
                line = lines[i].strip().split()
                if line[0] == id:
                    line[pos] = text
                    lines[i] = " ".join(line)+"\n"

    with open(file_name, 'w', encoding="utf-8") as f_w:
        f_w.writelines(lines)


def del_card(file_name):
    id = us.menu_for_del()
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("Файл пустой, удалять нечего")
            return 0
        i = 0
        while i < len(lines):
            if file_name[-3:] == "csv":
                line = lines[i].strip().split(';')
            else:
                line = lines[i].strip().split()

            if line[0] == id:
                print(line)
                value = us.menu2_for_del()
                if value == 1:
                    lines.remove(lines[i])
                    print("Строка удалена!")
                else:
                    print("Строка остается")
            i += 1
    with open(file_name, 'w', encoding="utf-8") as f_w:
        f_w.writelines(lines)
