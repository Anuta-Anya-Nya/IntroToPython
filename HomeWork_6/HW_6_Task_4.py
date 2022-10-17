# Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий,
# значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
# out
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
# 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']},
# 'В': {'Ю': ['Юнона Ветрякова']}}

def create_dict_name(lst_names):
    dct = {i[0]: [] for i in lst_names}
    for i in lst_names:
        dct[i[0]].append(i)
    return dct


def create_dict(*str):
    lst = sorted([i for i in str])
    dictionary = {}
    for i in range(len(lst)):
        for f in range(len(lst[i])):
            if lst[i][f] == " ":
                dictionary[lst[i][f+1]] = {}
                break
    for k in dictionary.keys():
        arr = []
        for i in range(len(lst)):
            for f in range(len(lst[i])):
                if lst[i][f-1] == ' ' and lst[i][f] == k:
                    arr.append(lst[i])
        dictionary[k] = create_dict_name(arr)
    return dictionary


print(create_dict("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
      "Анна Савельева", "Юнона Ветрякова", "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))


def create_dict2(*args):
    n_s_sort = {}
    for n_s in args:
        n_s_sort.setdefault(n_s.split()[1][0], {}).setdefault(
            n_s.split()[0][0], []).append(n_s)
    return n_s_sort
