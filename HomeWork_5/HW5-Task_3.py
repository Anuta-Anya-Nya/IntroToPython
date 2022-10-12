# крестики-нолики
from random import randint


def print_game(game_list):
    print('-------------------------------')
    print(
        f'|    {game_list[0]}    |    {game_list[1]}    |    {game_list[2]}    |')
    print('-------------------------------')
    print(
        f'|    {game_list[3]}    |    {game_list[4]}    |    {game_list[5]}    |')
    print('-------------------------------')
    print(
        f'|    {game_list[6]}    |    {game_list[7]}    |    {game_list[8]}    |')
    print('-------------------------------')


def who_first():
    print("Определяем, какой игрок ходит первым:")
    person = randint(0, 1)
    if person:
        print("Первым ходит игрок 2!")
    else:
        print("Первым ходит игрок 1!")
    return person


def is_right(number: str):
    result = number.isdigit() and int(number) > 0 and int(number) < 10
    return result


def game_rules(game_list, person):
    print(f'Ход игрока {person+1}:')
    number = input("Введите число от 1 до 9: ")
    while not is_right(number):
        print('Введены неверные данные!')
        number = input("Введите число от 1 до 9: ")
    number = int(number)

    if game_list[number-1] == number:
        if person:
            game_list[number-1] = chr(10060)
        else:
            game_list[number-1] = chr(11093)
    else:
        print("Указанное место уже занято!")
        game_rules(game_list, person)

    return game_list


def change_person(person):
    person = int(not bool(person))
    return person


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


def count_steps(count):
    count += 1
    return count


def start_game():
    my_game_list = [i for i in range(1, 10)]
    person = who_first()
    print_game(my_game_list)
    game_rules(my_game_list, person)
    person = change_person(person)
    count = count_steps(0)
    while not is_win(my_game_list, count):
        print_game(my_game_list)
        game_rules(my_game_list, person)
        person = change_person(person)
        count = count_steps(count)
    print_game(my_game_list)
    person = change_person(person)
    if count == 9:
        print("Ничья!!!")
    else:
        print(f"ура, выиграл игрок {person+1})")


start_game()
