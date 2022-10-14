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
