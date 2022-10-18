import user as us
import contacts as con
import convert as conv


def start():
    menu_value = us.start_menu()
    if menu_value == 1:
        con.write_contact()
    elif menu_value == 2:
        con.find_contact()
    else:
        conv.convert_file()
