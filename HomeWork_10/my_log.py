from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('logging.csv', 'a', encoding="utf-8") as file:
        file.write(
            f"{update.effective_user.first_name}-{update.effective_user.id} : {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} - {update.message.text}\n")

math_oper = {
    1: "+",
    2: "-",
    3: "*",
    4: "/",
    5: "**",
    6: "** 0.5",
    7: "//",
    8: "%"
}
def calc_log(a, b, oper, res, update: Update):
    day_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    with open('logging.csv', 'a', encoding="utf-8") as file:
        if oper == 6:
            file.write(
                f'{update.effective_user.first_name}-{update.effective_user.id} : {day_time} - Выражение: {a} {math_oper[oper]} = {res}\n')
        else:
            file.write(
                f'{update.effective_user.first_name}-{update.effective_user.id} : {day_time} - Выражение: {a} {math_oper[oper]} {b} = {res}\n')

def div_zero_log(a, b, update: Update):
    day_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    with open('logging.csv', 'a', encoding="utf-8") as file:
        file.write(f'{update.effective_user.first_name}-{update.effective_user.id} : {day_time} - Ошибка! {a} невозможно поделить на {b}!\n')


def sqrt_negat_log(a, update: Update):
    day_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    with open('logging.csv', 'a', encoding="utf-8") as file:
        file.write(
            f'{update.effective_user.first_name}-{update.effective_user.id} : {day_time} - Ошибка! Невозможно найти квадратный корень числа {a}!\n')