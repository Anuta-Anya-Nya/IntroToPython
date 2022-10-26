# python-telegram-bot версии 20.x
import logging
from random import randint
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler

# настроим модуль ведения журнала логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
FIRST = 0
PLAY = 1
person = 0
my_game_list = [i for i in range(1, 10)]
count = 0


def print_game(game_list):
    field = f"----------------\n| {game_list[0]} | {game_list[1]} | {game_list[2]} |\n----------------\n| {game_list[3]} | {game_list[4]} | {game_list[5]} |\n----------------\n| {game_list[6]} | {game_list[7]} | {game_list[8]} |\n----------------\n"
    return field


def is_win(game_list, count):
    result = (game_list[0] == game_list[1] and game_list[1] == game_list[2]) or (
        game_list[3] == game_list[4] and game_list[5] == game_list[4]) or (
        game_list[6] == game_list[7] and game_list[7] == game_list[8]) or (
        game_list[0] == game_list[3] and game_list[3] == game_list[6]) or (
        game_list[1] == game_list[4] and game_list[4] == game_list[7]) or (
        game_list[2] == game_list[5] and game_list[5] == game_list[8]) or (
        game_list[0] == game_list[4] and game_list[4] == game_list[8]) or (
        game_list[2] == game_list[4] and game_list[4] == game_list[6]) or count == 9
    return result


def change_person(person):
    person = int(not bool(person))
    return person


async def start(update, context):

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Привет, {update.effective_user.first_name}! Давай поиграем в крестики-нолики!")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Готовы играть? 1-да, 2-выход")
    return FIRST


async def first_step(update, context):
    global my_game_list, person, count
    user_answer = update.message.text
    if user_answer == '1':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Определяем, какой игрок ходит первым...")
        person = randint(0, 1)
        if person:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Первым ходит игрок 2!")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Первым ходит игрок 1!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=print_game(my_game_list))
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Ход игрока {}. Введите число от 1 до 9. Выход - 0".format(person+1))
        return PLAY
    elif user_answer == '2':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="До свидания!")
        return ConversationHandler.END
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введено неверное число, повторите ввод 1 или 2")


async def play_game(update, context):
    global my_game_list, person, count

    while not is_win(my_game_list, count):
        number = update.message.text
        if number in "1 2 3 4 5 6 7 8 9":
            number = int(number)
            if my_game_list[number-1] == number:
                if person:
                    my_game_list[number-1] = chr(10060)
                else:
                    my_game_list[number-1] = chr(11093)
                count += 1
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=print_game(my_game_list))
                if not is_win(my_game_list, count):
                    person = change_person(person)
                    await context.bot.send_message(chat_id=update.effective_chat.id,
                                                   text="Ход игрока {}. Введите число от 1 до 9. Выход - 0".format(person+1))
                    return PLAY
                else:
                    if count == 9:
                        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ничья")

                    else:
                        await context.bot.send_message(chat_id=update.effective_chat.id,
                                                       text=f"Игрок {person+1} выиграл!!!")
                    my_game_list = [i for i in range(1, 10)]
                    count = 0
                    return ConversationHandler.END
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id, text="Указанное место уже занято! Введите другое число от 1 до 9. Выход - 0")
                return PLAY
        elif number == '0':
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="До свидания!")
            my_game_list = [i for i in range(1, 10)]
            count = 0
            return ConversationHandler.END
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Введено неверное значение! Введите число от 1 до 9. Выход - 0")
            return PLAY


if __name__ == '__main__':
    TOKEN = '5608687961:AAGuhd3AEfSCjyrz39VDVTKf4du6yh_8Nk4'

    application = ApplicationBuilder().token(TOKEN).build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={FIRST: [MessageHandler(filters.TEXT, first_step)],
                PLAY: [MessageHandler(filters.TEXT, play_game)]},
        fallbacks=[])
    application.add_handler(conversation_handler)

    application.run_polling()
