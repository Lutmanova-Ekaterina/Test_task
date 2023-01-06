# 1
def func(list):    # функция перемещает нули в конец, сохраняя порядок символов
    c = 0  # сохраняет индекс следующей свободной позиции
    for i in list:
        if i == 0:
            c += 1
    new = list[c:] + list[:c]
    return new
print(func(list))


# 2
def sum_row(n: int):
    p_row: list[int] = [] # предыдущий ряд
    n_row: list[int] = [] # n-ряд
    if n > 1:
        for i in range(1, n * (n - 1), 2):  # при последовательности(начиная с 1) прибавляет 2 к каждому предыдущему числу
            p_row.append(i)
        for i in range(p_row[-1] + (n * 2) + 2, 2):  # получили n-ряд
            n_row.append(i)
    else:
        n_row.append(n)
    return sum(n_row)  # высчитываем сумму
print(sum_row())