from math import sin
from scipy.optimize import bisect


def function(x):
    y = sin(x)
    return y


# Ввод данных
print('Введите левый и правый конец интервала через пробел: ', end='')
start, stop = map(int, input().split())
step = float(input('Введите значечние шага: '))
eps = float(input('Введите точность: '))
max_iter = int(input('Введите максимальное количество итераций: '))
print()
sigma = 0.1
number = 0

# Метод секущих

print('Метод секущих')

table_flag = 0
i = start

# Основной цикл прохождения по отрезкам
while i < stop:
    error = 0
    flag = 0
    a = i
    if i + step > stop:
        b = stop
    else:
        b = i + step
    x0 = i
    x1 = x0 + 2 * eps
    f0 = function(x0)
    f1 = function(x1)

    for j in range(max_iter):

        if f1 - f0 == 0:
            x2 = (x0 * f1 - x1 * f0) / (f1 - f0 + 0.01)
        else:
            x2 = (x0 * f1 - x1 * f0) / (f1 - f0)

        x0, x1 = x1, x2
        f0, f1 = f1, function(x2)

        if abs(f1) < eps:
            flag = 1
            break

    if x1 < i or x1 > i + step:
        flag = 0
        x0 = i + step
        x1 = x0 - 2 * eps
        f0 = function(x0)
        f1 = function(x1)

        for j in range(max_iter):

            if f1 - f0 == 0:
                x2 = (x0 * f1 - x1 * f0) / (f1 - f0 + 0.01)
            else:
                x2 = (x0 * f1 - x1 * f0) / (f1 - f0)

            x0, x1 = x1, x2
            f0, f1 = f1, function(x2)

            if abs(f1) < eps:
                flag = 1
                break

    if f1 < 0:
        f1 = - f1

    if f1 < -0.01 or f1 > 0.01:
        error = 2
    if flag == 0:
        error = 1
    if x1 < i or x1 > i + step:
        x1 = '-'
        f1 = '-'
        error = 3

    # Вывод
    if error != 3:

        if table_flag == 0:
            # Начало таблицы вывода результатов
            print('┌', '─' * 81, '┐', sep='')
            print('│', ' ' * 34, 'Метод секущих', ' ' * 34, '│', sep='')
            print('├', '─' * 9, '┬', '─' * 21, '┬', '─' * 15, '┬',
                  '─' * 18, '┬', '─' * 14, '┤', sep='')
            print('│ № корня │       Отрезок       │  Знач. корня  │'
                  '  Знач. функциии  │  Код ошибки  │', sep='')
            table_flag = 1

        number += 1
        print('├', '─' * 9, '┼', '─' * 21, '┼', '─' * 15, '┼',
              '─' * 18, '┼', '─' * 14, '┤', sep='')
        print('│', '{:8d} '.format(number), '│', ' ' * 4,
              '({:6.2f}; {:6.2f}) '.format(a, b), '│',
              '{:14.4f} '.format(x1), '│', '{:17.0e} '.format(f1),
              '│', '{:13d} '.format(error), '│', sep='')

    i += step

if table_flag == 1:
    print('└', '─' * 9, '┴', '─' * 21, '┴', '─' * 15, '┴',
          '─' * 18, '┴', '─' * 14, '┘', sep='')
else:
    print('На данном отрезке нет корней.')
print()

# Scipy bisect

print('Scipy bisect')

table_flag = 0
number = 0
error = 0
i = start

# Основной цикл прохождения по отрезкам
while i < stop:
    a = i
    if i + step > stop:
        b = stop
    else:
        b = i + step

    try:
        x1 = bisect(function, a, b)
        f1 = function(x1)

        if f1 < 0:
            f1 = - f1

        if table_flag == 0:
            # Начало таблицы вывода результатов
            print('┌', '─' * 81, '┐', sep='')
            print('│', ' ' * 34, 'Scipy bisect', ' ' * 35, '│', sep='')
            print('├', '─' * 9, '┬', '─' * 21, '┬', '─' * 15, '┬',
                  '─' * 18, '┬', '─' * 14, '┤', sep='')
            print('│ № корня │       Отрезок       │  Знач. корня  │'
                  '  Знач. функциии  │  Код ошибки  │', sep='')
            table_flag = 1

        number += 1
        print('├', '─' * 9, '┼', '─' * 21, '┼', '─' * 15, '┼',
              '─' * 18, '┼', '─' * 14, '┤', sep='')
        print('│', '{:8d} '.format(number), '│', ' ' * 4,
              '({:6.2f}; {:6.2f}) '.format(a, b), '│',
              '{:14.4f} '.format(x1), '│', '{:17.0e} '.format(f1),
              '│', '{:13d} '.format(error), '│', sep='')
    except ValueError:
        pass

    i += step

if table_flag == 1:
    print('└', '─' * 9, '┴', '─' * 21, '┴', '─' * 15, '┴',
          '─' * 18, '┴', '─' * 14, '┘', sep='')
else:
    print('На данном отрезке нет корней.')

print()
print('Коды ошибок:')
print('0 - нет ошибок;')
print('1 - превышено максимальное количество итераций;')
# print('2 - ошибка метода, неточность;')
