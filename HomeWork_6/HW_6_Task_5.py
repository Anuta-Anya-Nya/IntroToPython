# Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

from random import randint


def rand_ind(lst):
    return randint(0, len(lst)-1)


def del_element(list_words, new_list):
    ind = rand_ind(list_words)
    new_list.append(list_words[ind])
    del list_words[ind]


def create_joke(n, replay=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра",
               "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(0, n):
        if replay:
            while len(nouns) > 0 and len(adverbs) > 0 and len(adjectives) > 0:
                arr = []
                del_element(nouns, arr)
                del_element(adverbs, arr)
                del_element(adjectives, arr)
                jokes.append(' '.join(arr))
        else:
            jokes.append(nouns[rand_ind(
                nouns)] + ' ' + adverbs[rand_ind(adverbs)] + ' ' + adjectives[rand_ind(adjectives)])
    return jokes


print(create_joke(10))

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра",
           "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def create_joke(n, replay=False):
    # делаем копии списков для удаления
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj)  # находим список с минимальной длиой

    while n and list_min:
        num = randrange(len(list_min))
        # Сразу в аппенд можно передать условие. pop удаляет и возвращает удаленное
        list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}" if repeat
                         else f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")  # choice дергает любое значение, тк не удаляет, то можно из исходных списков
        n -= 1
    return list_of_j
