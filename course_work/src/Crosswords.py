# num - матрица с номерами слов (размер такой же,
#                      как у обрабатываемого кроссворда)
# crosswords - массив, каждый элемент которого - кроссворд; элементы
#                      кроссворда - массивы из элементов строки
# crossword - элемент массива crosswords
# startNumI, startNumJ - координаты начала слова
# number - счетчик для номеров слов
# word - слово в кроссворде
# rows - количество строк кроссворда
# cols - количество столбцов кроссворда


# Функция, обрабатывающая кроссворды
def main_process(crossword):
    # матрица с номерами слов
    num = [[0] * len(crossword[0]) for i in range(len(crossword))]
    number = 1
    if crossword[0][0] != '*':
        num[0][0] = number
        number += 1
    word = ''
    startNumI = 0
    startNumJ = 0
    print('  По горизонтали:')

    # Номера слов и слова по горизонтали
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] != '*':
                if j == 0 and i != 0:
                    num[i][j] = number
                    number += 1
                    word = crossword[i][j]
                    startNumI = i
                    startNumJ = j
                elif crossword[i][j-1] == '*':
                    num[i][j] = number
                    number += 1
                    word = crossword[i][j]
                    startNumI = i
                    startNumJ = j
                elif j == 0:
                    word = crossword[i][j]
                    startNumI = i
                    startNumJ = j
                elif i == 0 and j != 0:
                    num[i][j] = number
                    number += 1
                    word += crossword[i][j]
                elif crossword[i-1][j] == '*':
                    num[i][j] = number
                    number += 1
                    word += crossword[i][j]
                else:
                    word += crossword[i][j]
            if (crossword[i][j] != '*' and j != (len(crossword[i]) - 1)\
                    and crossword[i][j+1] == '*') or\
                    (j == len(crossword[i]) - 1 and crossword[i][j] != '*'):
                print('    ', num[startNumI][startNumJ], '. ', word, sep='')
                word = ''


    # Слова по вертикали
    word = ''
    print('  По вертикали:')
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if (i == 0 or crossword[i-1][j] == '*') and crossword[i][j] != '*':
                word = crossword[i][j]
                startNumI = i
                startNumJ = j
                k = i + 1
                while k != len(crossword):
                    if crossword[k][j] != '*':
                        word += crossword[k][j]
                        k += 1
                    else:
                        break
                print('    ', num[startNumI][startNumJ], '. ', word, sep='')
                word = ''


# Основная программа
print('Введите количество строк и столбцов (через Enter),'
          ' а затем строки кроссворда или 0 для завершения ввода.')

# проверка на правильность ввода
rows = ''
while type(rows) != int:
    try:
        rows = int(input())
    except ValueError:
        print('Неправильный ввод! Попробуйте снова!')

# Получаем массив из кроссвордов.
# Каждый элемент массива crosswords - это массив строк каждого
# из кроссвордов
crosswords = []
while rows != 0:
    # проверка на правильность ввода
    cols = ''
    while type(cols) != int:
        try:
            cols = int(input())
        except ValueError:
            print('Неправильный ввод!')

    a = [[] for i in range(rows)]
    for i in range(rows):
        while len(a[i]) != cols:
            a[i] = input() # ввод строки кроссворда
            if len(a[i]) != cols:
                print('Количество символов должно быть'
                          ' равно {}. Попробуйте снова!'.format(cols))
    crosswords.append(a)
    print('Введите количество строк и столбцов (через Enter),'
              ' а затем строки кроссворда или 0 для завершения ввода.')

    # проверка на правильность ввода
    rows = ''
    while type(rows) != int:
        try:
            rows = int(input())
        except ValueError:
            print('Неправильный ввод! Попробуйте снова!')

# Преобразуем массив:
# строку кроссворда меняем на массив из символов этой строки
for i in range(len(crosswords)):
    for j in range(len(crosswords[i])):
        b = []
        for k in range(len(crosswords[i][j])):
            x = crosswords[i][j][k:k+1]
            b.append(x)
        crosswords[i][j] = b

# Выполняем функцию main_process для каждого введенного кроссворда
for i in range(len(crosswords)):
    print('Кроссворд №{}:'.format(i+1))
    main_process(crosswords[i])
    print()