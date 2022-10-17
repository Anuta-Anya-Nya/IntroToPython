# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка",
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

from itertools import groupby


def create_dict(*str):
    lst_names = sorted([i for i in str])
    dct = {i[0]: [] for i in lst_names}
    for i in lst_names:
        dct[i[0]].append(i)

    return dct


print(create_dict("Иван", "Мария", "Петр", "Илья",
      "Марина", "Петр", "Алина", "Бибочка", "Аня", "Роман"))

# dict ={}
# for i in sorted(str):
#     letter=i[0]
#     if letter in dict:
#         dict[letter]+=[i] список расширяется этим значением списка
#     else:
#         dict[letter]=[i] создается пара ключ\значение


def create_d(*args):
    if "" not in args:  # защита от пустоты
        # list comprehension для словаря.GROUPBY соберет группы по первой букве ch, мы оборачиваем это в списки. если такая буква есть
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


def create_d2(*args):
    if "" not in args:
        # comprehension для словаря. ключ первая буква из списка имен.
        # startswith(ch[0]) Возвращает флаг, указывающий на то, начинается ли строка с указанного префикса.
        return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
    return "Error"
