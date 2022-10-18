import user_interface as user
import operation as op
import compl
import excep as ex
import log


def start_calc():
    while True:
        format_num = user.choose_format()

        if format_num == 1:
            number_1 = user.enter_value_ration(1)
            number_2 = user.enter_value_ration(2)
            operat = user.menu_ration()
            ex.sqrt_negat(operat, number_1)
        else:
            number_1 = compl.get_compl_numb(
                user.enter_value_compl_d(1), user.enter_value_compl_m(1))
            user.print_compl_num(1, number_1)
            number_2 = compl.get_compl_numb(
                user.enter_value_compl_d(2), user.enter_value_compl_m(2))
            user.print_compl_num(2, number_2)
            operat = user.menu_compl()
        if operat:
            break
    ex.div_zero(operat, number_1, number_2)
    result = op.calc(operat, number_1, number_2)
    user.print_result(result)
    log.calc_log(number_1, number_2, operat, result)
