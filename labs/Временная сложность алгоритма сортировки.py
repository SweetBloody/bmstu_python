import random as rn


# Вставка с барьером
def insertionSortWithBarrier(arr):
    import time
    start_time = time.time()

    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[0] = arr[i]
        j = i - 1
        while arr[0] < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = arr[0]

    stop_time = time.time()
    time = stop_time - start_time
    return arr[1:], time

def sortTime(arr):
    import time
    start_time = time.time()
    arr.sort()
    stop_time = time.time()
    time = stop_time - start_time
    return arr, time

def printTableIncident(time):
    print('│', ' ' * 20, '│', ' ' * 9, 'Случайное расположение', ' ' * 10,
      '│', '{:25.9f} '.format(time), '│', sep='')

def printTableIncrease(time, length, word):
    if word == 'medium':
        print('│', ' ' * 2, '{} = {:6d}'.format(word, length), ' ' * 3, '│', ' ' * 8,
      'Упорядочен по возрастанию', ' ' * 8, '│', '{:25.9f} '.format(time),
      '│', sep='')
    else:
        print('│', ' ' * 3, '{} = {:6d}'.format(word, length), ' ' * 3, '│', ' ' * 8,
      'Упорядочен по возрастанию', ' ' * 8, '│', '{:25.9f} '.format(time),
      '│', sep='')

def printTableDecrease(time):
    print('│', ' ' * 20, '│', ' ' * 9, 'Упорядочен по убыванию', ' ' * 10,
      '│', '{:25.9f} '.format(time), '│', sep='')

def printTableBetween():
    print('│', ' ' * 20, '├', '─' * 41, '┼', '─' * 26, '┤', sep='')

def printTableEnd():
    print('├', '─' * 20, '┼', '─' * 41, '┼', '─' * 26, '┤', sep='')


# Вставка с барьером
print('------------------')
print('Вставка с барьером')
print('------------------')
print('Введите 3 значения размерности для массивов.')

# Ввод данных
small = int(input('Малое значение: '))
medium = int(input('Среднее значение: '))
large = int(input('Большое значение: '))

# Создание массивов
arr_s = [rn.randint(0, 100) for i in range(small)]
arr_m = [rn.randint(0, 100) for j in range(medium)]
arr_l = [rn.randint(0, 100) for k in range(large)]

# Начало таблицы "Вставка с барьером"
print('┌', '─' * 89, '┐', sep='')
print('│', ' ' * 35, 'Вставка с барьером', ' ' * 36, '│', sep='')
print('├', '─' * 20, '┬', '─' * 41, '┬', '─' * 26, '┤', sep='')
print('│', ' ' * 3, 'Размер массива', ' ' * 3, '│', ' ' * 9,
      'Упорядоченность массива', ' ' * 9, '│', ' ' * 7, 'Время работы',
      ' ' * 7, '│', sep='')
printTableEnd()


# Сортировка arr_small

# случайное расположение
arr_s, time = insertionSortWithBarrier(arr_s)
printTableIncident(time)
printTableBetween()

# упорядочен по возрастанию
arr_s, time = insertionSortWithBarrier(arr_s)
printTableIncrease(time, small, 'small')
printTableBetween()

# упорядочен по убыванию
arr_s.reverse()
arr_s, time = insertionSortWithBarrier(arr_s)
printTableDecrease(time)
printTableEnd()


# Сортировка arr_medium

# случайное расположение
arr_m, time = insertionSortWithBarrier(arr_m)
printTableIncident(time)
printTableBetween()

# упорядочен по возрастанию
arr_m, time = insertionSortWithBarrier(arr_m)
printTableIncrease(time, medium, 'medium')
printTableBetween()

# упорядочен по убыванию
arr_m.reverse()
arr_m, time = insertionSortWithBarrier(arr_m)
printTableDecrease(time)
printTableEnd()


# Сортировка arr_large

# случайное расположение
arr_l, time = insertionSortWithBarrier(arr_l)
printTableIncident(time)
printTableBetween()

# упорядочен по возрастанию
arr_l, time = insertionSortWithBarrier(arr_l)
printTableIncrease(time, large, 'large')
printTableBetween()

# упорядочен по убыванию
arr_l.reverse()
arr_l, time = insertionSortWithBarrier(arr_l)
printTableDecrease(time)
printTableEnd()


# Метод sort
print()
print('----------')
print('Метод sort')
print('----------')
print('Введите 3 значения размерности для массивов.')

# Ввод данных
small = int(input('Малое значение: '))
medium = int(input('Среднее значение: '))
large = int(input('Большое значение: '))

# Создание массивов
arr_s = [rn.randint(0, 100) for i in range(small)]
arr_m = [rn.randint(0, 100) for j in range(medium)]
arr_l = [rn.randint(0, 100) for k in range(large)]

# Начало таблицы "Метод sort"
print('┌', '─' * 89, '┐', sep='')
print('│', ' ' * 39, 'Метод sort', ' ' * 40, '│', sep='')
print('├', '─' * 20, '┬', '─' * 41, '┬', '─' * 26, '┤', sep='')
print('│', ' ' * 3, 'Размер массива', ' ' * 3, '│', ' ' * 9,
      'Упорядоченность массива', ' ' * 9, '│', ' ' * 7, 'Время работы',
      ' ' * 7, '│', sep='')
printTableEnd()

# Сортировка arr_small

# случайное расположение
arr_s, time = sortTime(arr_s)
printTableIncident(time)
printTableBetween()

# упорядочен по возрастанию
arr_s, time = sortTime(arr_s)
printTableIncrease(time, small, 'small')
printTableBetween()

# упорядочен по убыванию
arr_s.reverse()
arr_s, time = sortTime(arr_s)
printTableDecrease(time)
printTableEnd()


# Сортировка arr_medium

# случайное расположение
arr_m, time = sortTime(arr_m)
printTableIncident(time)
printTableBetween()

# упорядочен по возрастанию
arr_m, time = sortTime(arr_m)
printTableIncrease(time, medium, 'medium')
printTableBetween()

# упорядочен по убыванию
arr_m.reverse()
arr_m, time = sortTime(arr_m)
printTableDecrease(time)
printTableEnd()


# Сортировка arr_large

# случайное расположение
arr_l, time = sortTime(arr_l)
printTableIncident(time)
printTableBetween()

# упорядочен по возрастанию
arr_l, time = sortTime(arr_l)
printTableIncrease(time, large, 'large')
printTableBetween()

# упорядочен по убыванию
arr_l.reverse()
arr_l, time = sortTime(arr_l)
printTableDecrease(time)
printTableEnd()
