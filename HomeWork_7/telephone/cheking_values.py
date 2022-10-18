def cheking_menu(value):
    if value.isdigit():
        number = int(value)
        if 0 < number < 4:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def format_file(value):
    if value[-4] == '.':
        return True
    else:
        return False


def cheking_tel(value):
    return value.isdigit()
