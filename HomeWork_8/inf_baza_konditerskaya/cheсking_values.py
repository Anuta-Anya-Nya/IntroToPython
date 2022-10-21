def cheсking_menu(value):
    if value.isdigit():
        number = int(value)
        if 0 < number < 7:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def cheсking_menu_find(value):
    if value.isdigit():
        number = int(value)
        if 0 < number < 9:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def format_file(value):
    if value[-4:] == '.txt' or value[-4:] == '.csv':
        return True
    else:
        return False


def cheсking_number(value):
    return value.isdigit()


def format_file_conv(value):
    if value == 'txt' or value == 'csv':
        return True
    else:
        return False


def cheсking_menu_edit(value):
    if value.isdigit():
        number = int(value)
        if 0 < number < 8:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def checking_gender(value):
    if value.lower() == "муж" or value.lower() == "жен":
        return True
    else:
        return False
