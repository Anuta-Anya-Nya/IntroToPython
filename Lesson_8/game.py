import logging
from info import token
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters, ConversationHandler)
from random import shuffle, randint

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Определяем константы выполняемых этапов
CHOICE = 0
PLAY = 1
CANDIES = 121
CANDIES_LIMIT = 28
active_player = ""
players = []


def start(update, _):
    update.message.reply_text(
        f'Привет, {update.effective_user.first_name}, это - игра с конфетами.\n')
    update.message.reply_text(
        '1 - play with bot; \n2 - play with person; \n3 - stop the game :( \n')
    return CHOICE


def choice(update, context):
    global active_player, players
    # инфо для логера
    user = update.message.from_user
    logger.info(f"Выбор операции: {user.first_name}: {update.message.text}")

    user_choice = update.message.text
    if user_choice in '1 2 3':
        if user_choice in '1 2':
            players = ["human", 'bot' if user_choice < "2" else 'person']
            shuffle(players)
            active_player = players[0]
            return play_game(update, context)

        elif user_choice == '3':
            update.message.reply_text('Goodbye! It was nice to play :)')
            return ConversationHandler.END
    else:
        update.message.reply_text(
            "Don't forget to choose\n1 - play with bot; \n2 - play with person; \n3 - stop the game :( \n")


def play_game(update, context):
    global CANDIES, active_player, players

    while CANDIES > 0:
        update.message.reply_text(
            f'\nThere are {CANDIES} sweets on the table, you can take [1 .. {CANDIES_LIMIT}]')
        update.message.reply_text(f"Player {active_player}'s move")

        if active_player == "bot":
            get_candies = bot_run(CANDIES)
            update.message.reply_text(f'The bot took {get_candies} candies')
        else:
            update.message.reply_text(
                f'How many candies do you want {active_player}: ')
            get_candies = int(update.message.text)

        CANDIES -= get_candies
        if CANDIES > 0:
            active_player = moves(active_player)
            return PLAY
        else:
            update.message.reply_text(f'The player {active_player} won!')


def bot_run(candies):
    result = candies % 29
    if not result:
        result = randint(1, 28)
    return result


def moves(pl_act):
    global players
    first, second = players
    return second if pl_act == first else first


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями CHOICE, PLAY
    conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={CHOICE: [MessageHandler(Filters.text, choice)],
                PLAY: [MessageHandler(Filters.text, play_game)]},
        fallbacks=[])
    # точка выхода из разговора
    # fallbacks=[CommandHandler('stop', stop)],  )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
