# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
from random import choices


def create_words(number, word):
    words = []
    if number < 1:
        print('The data is incorrect')
        return ""
    for i in range(number):
        letters = choices(word, k=3)
        words.append(''.join(letters))
    return ' '.join(words)


def del_word(string_words, word):
    if not string_words:
        print('The data is incorrect')
        return ""
    list_words = string_words.split()
    list_words = list(filter(lambda x: not x == word, list_words))
    return " ".join(list_words)


my_string = create_words(int(input("Number of words: ")), 'abc')
print(my_string)
print(del_word(my_string, input("delete word: ")))
