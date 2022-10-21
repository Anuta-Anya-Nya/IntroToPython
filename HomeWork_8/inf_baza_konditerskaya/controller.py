import user as us
import cards
import convert as conv


def start():
    file_name = us.ask_file_name()

    while True:
        id_number = cards.find_id(file_name)
        menu_value = us.start_menu()
        match menu_value:
            case 1:
                cards.view_card(file_name)
            case 2:
                cards.write_card(file_name, id_number)
            case 3:
                us.print_find(cards.find_card(file_name))
            case 4:
                cards.edit_card(file_name)
            case 5:
                cards.del_card(file_name)
            case _:
                conv.convert_file()
