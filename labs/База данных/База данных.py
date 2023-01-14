import pickle as p


# Функция создания БД
def create_database():
    filename = input('Введите название файла:\n')
    f = open(filename, 'w')
    f.close()
    databaseName = input('Введите имя базы данных:\n')
    return filename, databaseName


# Функция добавления записи в БД
def string_addition(filename, databaseName):
    f = open(filename, 'rb')
    structure = {'book': 'a', 'author': 'a', 'year': '1'}
    print('Добавление записи в базу данных "{}".'.format(databaseName))
    structure['book'] = input('Введите название книги:\n')
    structure['author'] = input('Введите имя автора:\n')
    structure['year'] = input('Введите год выпуска:\n')
    flag = 0
    try:
        try:
            while f != '\0':
                structure_ver = p.load(f)
                if structure_ver['book'] == structure['book'] and\
                    structure_ver['author'] == structure['author'] and\
                    structure_ver['year'] == structure['year']:
                    flag = 1
        except EOFError:
            pass
        f.close()
        f = open(filename, 'ab')
        if flag == 0:
            p.dump(structure, f)
        else:
            print('Введенная строка уже существует в базе данных!')
    except Exception:
        print('Ошибка!')
    f.close()


# Функция вывода БД
def print_database(filename, databaseName):
    f = open(filename, 'rb')
    print('База данных "{}".'.format(databaseName))
    try:
        print('│', '—' * 25, '│', '—' * 20, '│', '—' * 8, '│', sep='')
        try:
            while f != '\0':
                structure = p.load(f)
                print('│', ' {:24}'.format(structure['book']), '│',
                      ' {:19}'.format(structure['author']), '│',
                      ' {:7}'.format(structure['year']), '│', sep='')
                print('│', '—' * 25, '│', '—' * 20, '│', '—' * 8, '│', sep='')
        except EOFError:
            pass
    except Exception:
        print('Ошибка!')
    f.close()


# Функция поиска по одному полю
def find_one_string(filename, databaseName):
    f = open(filename, 'rb')
    print('База данных "{}".'.format(databaseName))
    word = ''
    key = ''
    while word == '' or key == '':
        key = input('Введите ключ поля:\n')
        word = input('Введите слово, по которому будет производиться поиск:\n')
        if word == '' or key == '':
            print('Попробуйте еще раз!')
    flag = 0
    flag1 = 0
    try:
        try:
            while f != '\0':
                structure = p.load(f)
                if structure[key] == word:
                    if flag == 0:
                        print('│', '—' * 25, '│', '—' * 20, '│', '—' * 8, '│', sep='')
                    print('│', ' {:24}'.format(structure['book']), '│',
                          ' {:19}'.format(structure['author']), '│',
                          ' {:7}'.format(structure['year']), '│', sep='')
                    print('│', '—' * 25, '│', '—' * 20, '│', '—' * 8, '│', sep='')
                    flag1 = 1
                flag = 1
        except EOFError:
            pass
    except Exception:
        print('Ошибка!')
    else:
        if flag1 == 0:
            print('Нет таких записей!')
    f.close()


# Функция поиска по двум полям
def find_two_strings(filename, databaseName):
    f = open(filename, 'rb')
    print('База данных "{}".'.format(databaseName))
    word1 = ''
    key1 = ''
    word2 = ''
    key2 = ''
    while word1 == '' or key1 == '':
        key1 = input('Введите ключ первого поля:\n')
        word1 = input('Введите слово, по которому будет производиться поиск:\n')
        if word1 == '' or key1 == '':
            print('Попробуйте еще раз!')
    while word2 == '' or key2 == '':
        key2 = input('Введите ключ второго поля:\n')
        word2 = input('Введите слово, по которому будет производиться поиск:\n')
        if word2 == '' or key2 == '':
            print('Попробуйте еще раз!')
    flag = 0
    flag1 = 0
    try:
        try:
            while f != '\0':
                structure = p.load(f)
                if structure[key1] == word1 and structure[key2] == word2:
                    if flag == 0:
                        print('│', '—' * 25, '│', '—' * 20, '│', '—' * 8, '│', sep='')
                    print('│', ' {:24}'.format(structure['book']), '│',
                          ' {:19}'.format(structure['author']), '│',
                          ' {:7}'.format(structure['year']), '│', sep='')
                    print('│', '—' * 25, '│', '—' * 20, '│', '—' * 8, '│', sep='')
                    flag1 = 1
                flag = 1
        except EOFError:
            pass
    except Exception:
        print('Ошибка!')
    else:
        if flag1 == 0:
            print('Нет таких записей!')
    f.close()


# Основная программа
choice = 1
filename = 'DataBase'
databaseName = 'книги'
while choice != 0:
    print('Меню.')
    print('1. Создание БД.')
    print('2. Добавление записи в БД.')
    print('3. Вывод всей БД.')
    print('4. Поиск записей по одному полю.')
    print('5. Поиск записей по двум полям.')
    print('0. Выход.')
    try:
        choice = int(input('Выберите пункт меню:\n'))
    except ValueError:
        choice = 6
    if choice < 0 or choice > 5:
        print('Неверный выбор. Нужно ввести цифру от 1 до 8. '
              'Попробуйте снова!')
    elif choice == 1:
        filename, databaseName = create_database()
    elif choice == 2:
        try:
            string_addition(filename, databaseName)
        except FileNotFoundError:
            print('Вы не ввели название файла в пункте 1!')
    elif choice == 3:
        try:
            print_database(filename, databaseName)
        except FileNotFoundError:
            print('Вы не ввели название файла в пункте 1!')
    elif choice == 4:
        try:
            find_one_string(filename, databaseName)
        except FileNotFoundError:
            print('Вы не ввели название файла в пункте 1!')
    elif choice == 5:
        try:
            find_two_strings(filename, databaseName)
        except FileNotFoundError:
            print('Вы не ввели название файла в пункте 1!')
    elif choice == 0:
        pass
