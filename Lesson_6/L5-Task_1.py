# посчитать строку с математическим выражением
actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


res = '( 10 + 5 ) * 3 - 8 / 2'


def scob(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] == '(':  # если попался элемент скобка, то
            # взяли индекс закрывающей скобки с индекса i
            m = line.index(')', i)
            # добавили в массив список выражения без скобок для приоритетности
            lst.append(line[i+1:m])
            i = m  # передвинули счетчик на скобку, пропустив срез с выражением
        else:
            lst.append(line[i])
        i += 1
    return lst


def in_scob(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            a, b, c = scob(lst[i])
            lst[i] = actions[b](a, c)
    return lst


print(in_scob(scob(res.split())))


def result(lst):
    # собираем спиок из индекса i элемента j если он */
    prior = [i for i, j in enumerate(lst) if j in '*/']
    while prior:  # пока такие элементы деления умножения есть
        t = prior[0]  # берем первый индекс / или *
        # распаковываем цифру до и после и знак в переменные
        a, b, c = lst[t-1: t+2]
        # добавляем перед выражением посчитанное число  вформате строки
        lst.insert(t-1, actions[b](a, c))
        del lst[t: t+3]  # удаляем старое выражение. индексы сдвинулись на 1
        # проверяем есть ли еще / и *
        prior = [i for i, j in enumerate(lst) if j in '*/']

    while len(lst) > 1:
        a, b, c = lst[: 3]
        del lst[: 3]
        lst.insert(0, actions[b](a, c))
    return lst


print(result(in_scob(scob(res.split()))))


# set defaut 4
#
