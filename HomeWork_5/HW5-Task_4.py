# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
from random import randint


def who_first():
    print("Определяем, какой игрок ходит первым:")
    person = randint(0, 1)
    if person:
        print("Первым ходит игрок 2!")
    else:
        print("Первым ходит игрок 1!")
    return person


def is_right(number: str):
    result = number.isdigit() and int(number) > 0 and int(number) < 29
    return result


def is_right_option(number: str):
    result = number.isdigit() and int(number) > 0 and int(number) < 3
    return result


def change_person(person):
    person = int(not bool(person))
    return person


def game_persons(candies, person):
    print(f'Ход игрока {person+1}.', end=" ")
    number = input("Введите число от 1 до 28: ")
    while not is_right(number):
        print('Введены неверные данные!')
        number = input("Введите число от 1 до 28: ")
    number = int(number)
    candies = candies - number
    print(f'Осталось {candies} конфет.')
    return candies


def play_the_game_human():
    person = who_first()
    candies = 107
    print(f'На столе {candies} конфет.')
    while candies > 0:
        candies = game_persons(candies, person)
        person = change_person(person)
    person = change_person(person)
    print(f'Победа!!! Выиграл игрок {person+1}!!!')


def who_first_bot():
    print("Определяем, кто ходит первым:")
    person = randint(0, 1)
    if person:
        print("Первым ходит игрок 1!")
    else:
        print("Первым ходит бот!")
    return person


def find_numb_bot(candies):
    if candies % 29:
        number = candies % 29
    else:
        # т.к. 0 конфет брать нельзя, вщзьмем рандомное число
        number = randint(1, 29)
    return number


def game_bot(candies, person):
    if person:
        print(f'Ход игрока.', end=" ")
        number = input("Введите число от 1 до 28: ")
        while not is_right(number):
            print('Введены неверные данные!')
            number = input("Введите число от 1 до 28: ")
        number = int(number)
    else:
        print(f'Ход бота.', end=" ")
        number = find_numb_bot(candies)
        print(f"Введите число от 1 до 28: {number}")

    candies = candies - number
    print(f'Осталось {candies} конфет.')
    return candies


def play_the_game_bot():
    person = who_first_bot()
    candies = 107
    print(f'На столе {candies} конфет.')
    while candies > 0:
        candies = game_bot(candies, person)
        person = change_person(person)
    person = change_person(person)
    if person:
        print('Победа!!! Выиграл игрок!!!')
    else:
        print('Победа!!! Выиграл бот!!!')


def start_game():
    print('Выберите режим игры: 1 - между игроками, 2 - с ботом.')
    select_option = input('Режим: ')
    while not is_right_option(select_option):
        print('Введены неверные данные!')
        select_option = input("Введите число 1 или 2: ")
    select_option = int(select_option)
    if select_option == 1:
        print('Выбран режим игры между игроками.')
        play_the_game_human()
    else:
        print('Выбран режим игры с ботом.')
        play_the_game_bot()


start_game()
