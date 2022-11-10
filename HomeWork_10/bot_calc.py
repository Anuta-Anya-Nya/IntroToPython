import my_token
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler
import my_log

# настроим модуль ведения журнала логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
FIRST, START_CALC, CALC_RATION_1, CALC_RATION_2, CALC_COM_1D, CALC_COM_1M, CALC_COM_2D, CALC_COM_2M, USE_CALC = range(9)
number_format = 0
numb_1 = 0
numb_2 = 0


math_operations = {
    1: lambda x, y: x+y,
    2: lambda x, y: x-y,
    3: lambda x, y: x*y,
    4: lambda x, y: x/y,
    5: lambda x, y: x**y,
    6: lambda x, y: x**0.5,
    7: lambda x, y: x//y,
    8: lambda x, y: x % y
}


def calc(numb_oper, a, b):
    return math_operations[numb_oper](a, b)


def enter_value_ex(number):
    return number.strip("-").replace(".", "").isdigit()


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


        


async def start(update, context):
    my_log.log(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Привет, {update.effective_user.first_name}! Тебе нужна помощь калькулятора?")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="1 - да\n2 - нет")
    return FIRST


async def what_format(update, context):
    my_log.log(update, context)
    user_answer = update.message.text
    if user_answer == '1':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Давай определимся, с каким форматом чисел будем работать")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="1 - рациональное \n2 - комплексное \nq - выход")
        return START_CALC
    elif user_answer == '2':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Хорошо, до свидания!")
        return ConversationHandler.END 
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число, повтори ввод 1 или 2")

async def start_calc(update, context):    
    global number_format
    my_log.log(update, context)
    user_answer = update.message.text
    if user_answer == '1':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Использую калькулятор для рациональных чисел")
        number_format = 1
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи первое число")                                           
        return CALC_RATION_1
    elif user_answer == '2':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Использую калькулятор для комплексных чисел")
        number_format = 2
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи действительную часть первого числа")        
        return CALC_COM_1D
    elif user_answer == 'q':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Хорошо, до свидания!")
        return ConversationHandler.END 
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число, повтори ввод 1, 2 или q")   

async def calc_rat_1 (update, context):
    global numb_1
    my_log.log(update, context)
    value=update.message.text
    while not enter_value_ex(value):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи первое число")
        return CALC_RATION_1
    numb_1 = eval(value)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи второе число")
    return CALC_RATION_2


async def calc_rat_2 (update, context):
    global numb_2
    my_log.log(update, context)
    value=update.message.text
    while not enter_value_ex(value):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи второе число")
        return CALC_RATION_2
    numb_2 = eval(value)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Выбери математическую операцию:\n\
    1 - сложение\n\
    2 - вычитание\n\
    3 - умножение\n\
    4 - деление\n\
    5 - возведение в степень\n\
    6 - извлечение квадратного корня\n\
    7 - целочисленное деление\n\
    8 - остаток от деления\n\
    0 - предыдущее меню\n\
    q - выход")
    return USE_CALC


async def calc_compl_1d (update, context):
    global numb_1
    my_log.log(update, context)
    value=update.message.text
    while not enter_value_ex(value):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи действительную часть первого числа")
        return CALC_COM_1D
    numb_1 = eval(value)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи мнимую часть первого числа")
    return CALC_COM_1M

async def calc_compl_1m (update, context):
    global numb_1
    my_log.log(update, context)
    value=update.message.text
    while not enter_value_ex(value):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи мнимую часть первого числа")
        return CALC_COM_1M
    numb_1 = complex(numb_1, eval(value))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Первое комплексное число: {numb_1}")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи действительную часть второго числа")
    return CALC_COM_2D


async def calc_compl_2d (update, context):
    global numb_2
    my_log.log(update, context)
    value=update.message.text
    while not enter_value_ex(value):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи действительную часть второго числа")
        return CALC_COM_2D
    numb_2 = eval(value)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи мнимую часть второго числа")
    return CALC_COM_2M

async def calc_compl_2m (update, context):
    global numb_2
    my_log.log(update, context)
    value=update.message.text
    while not enter_value_ex(value):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи мнимую часть второго числа")
        return CALC_COM_2M
    numb_2 = complex(numb_2, eval(value))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Второе комплексное число: {numb_2}")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Выберите математическую операцию:\n\
    1 - сложение\n\
    2 - вычитание\n\
    3 - умножение\n\
    4 - деление\n\
    5 - возведение в степень\n\
    6 - извлечение квадратного корня\n\
    0 - предыдущее меню\n\
    q - выход")
    return USE_CALC


async def use_calc (update, context):
    value = update.message.text
    my_log.log(update, context)
    if number_format == 1:
        while not menu_ration_ex(value):
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Выбери математическую операцию для рационального числа")
            return USE_CALC
    else: 
        while not menu_compl_ex(value):
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число!")
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Выбери математическую операцию для комплексного числа")
            return USE_CALC
    if value == 'q':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="До свидания!")
        return ConversationHandler.END
    elif value == '0':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Переходим к предыдущему меню")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Давай определимся, с каким форматом чисел будем работать")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="1 - рациональное \n2 - комплексное \nq - выход")
        return START_CALC

    operat = int(value)
    if (operat == 4 or operat == 7 or operat == 8) and numb_2 == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Невозможная операция!")
        my_log.div_zero_log(numb_1, numb_2, update)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Желаешь продолжить?")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="1 - да\n2 - нет")                                  
        return FIRST
    if number_format == 1 and operat == 6 and numb_1 < 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Невозможная операция!")
        my_log.sqrt_negat_log(numb_1, update)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Желаешь продолжить?")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="1 - да\n2 - нет")                                  
        return FIRST
    result = calc(operat, numb_1, numb_2)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Получен результат: {result}")
    my_log.calc_log(numb_1, numb_2, operat, result, update)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Желаешь продолжить?")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="1 - да\n2 - нет")                                  
    return FIRST


if __name__ == '__main__':
    # TOKEN = ''

    application = ApplicationBuilder().token(my_token.TOKEN).build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={FIRST: [MessageHandler(filters.TEXT, what_format)],
                START_CALC: [MessageHandler(filters.TEXT, start_calc)],
                CALC_RATION_1: [MessageHandler(filters.TEXT, calc_rat_1)],                
                CALC_RATION_2: [MessageHandler(filters.TEXT, calc_rat_2)],
                CALC_COM_1D: [MessageHandler(filters.TEXT, calc_compl_1d)],
                CALC_COM_1M: [MessageHandler(filters.TEXT, calc_compl_1m)],
                CALC_COM_2D: [MessageHandler(filters.TEXT, calc_compl_2d)],
                CALC_COM_2M: [MessageHandler(filters.TEXT, calc_compl_2m)],
                USE_CALC: [MessageHandler(filters.TEXT, use_calc)]},
        fallbacks=[])
    application.add_handler(conversation_handler)

    application.run_polling()
