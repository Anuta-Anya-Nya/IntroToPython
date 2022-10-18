import sys
import log


def choose_format_ex(value):
    if value.isdigit():
        number = int(value)
        if 0 <= number < 3:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def menu_ration_ex(value):
    if value.isdigit():
        number = int(value)
        if 0 <= number < 9:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def menu_compl_ex(value):
    if value.isdigit():
        number = int(value)
        if 0 <= number < 7:
            return True
        else:
            return False
    elif value == 'q':
        return True
    else:
        return False


def enter_value_ex(number):
    return number.strip("-").replace(".", "").isdigit()


def div_zero(num_operat, num_1, num_2):
    if (num_operat == 4 or num_operat == 7 or num_operat == 8) and num_2 == 0:
        print("Невозможная операция, на ноль делить нельзя!")
        log.div_zero_log(num_1, num_2)
        sys.exit()


def sqrt_negat(num_operat, number):
    if num_operat == 6 and number < 0:
        # в рациаональных нельзя брать корень из отрицательноо числа
        print("Невозможная операция!")
        log.sqrt_negat_log(number)
        sys.exit()
