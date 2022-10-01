# Задайте список, состоящий из произвольных слов, количество задает пользователь.
# напишите программу, которая определит индекс второго вхождения строки в списле, или сообщет, что ее нет
from random import choices


def compose_words(count, word):
    words_list = []
    for i in range(count):
        # список составили из 3 букв, k внутренний параметр количество
        y = choices(word, k=3)
        # склеили список в слово и добавили в конец списка list
        words_list.append(''.join(y))
    return words_list


def find_word(word, some_list):
    if some_list.count(word) > 1:
        first_index = some_list.index(word)
        print(some_list.index(word, first_index+1))
    else:
        print('-1')


test_list = compose_words(30, 'xyz')
print(test_list)
find_word(input(), test_list)
