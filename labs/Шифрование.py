def lat_dict():
    dict = {}
    k = 32
    for i in range(0, 91):
        dict[i] = chr(k)
        k += 1
    return dict


def kir_dict():
    dict = {}
    k = 32
    for i in range(0, 32):
        dict[i] = chr(k)
        k += 1
    k = 1040
    for i in range(32, 96):
        dict[i] = chr(k)
        k += 1
    dict[96] = chr(1105)
    dict[97] = chr(1025)
    return dict


def dict_choice():
    print('Выберете алфавит:\n1. Латинский\n2. Русский')
    choice1 = float(input('Выбор: '))
    dictionary = {}
    num = 0
    if choice1 != 1 and choice1 != 2:
        print('Неверный выбор. Нужно ввести цифру 1 или 2.'
              'Попробуйте снова!\n')
        dict_choice()
    elif choice1 == 1:
        dictionary = lat_dict()
        num = 91
    elif choice1 == 2:
        dictionary = kir_dict()
        num = 98
    return dictionary, num


def encode_value(word, dictionary):
    code = []
    for i in range(len(word)):
        for val in dictionary:
            if word[i] == dictionary[val]:
                code.append(val)
    return code


def decode_word(code, dictionary):
    word = ''
    for i in range(len(code)):
        word += dictionary[code[i]]
    return word


def encode(wordCode, keyCode, num):
    code = []
    k = 0
    for i in range(len(wordCode)):
        c = (wordCode[i] + keyCode[k % len(keyCode)]) % num
        k += 1
        code.append(c)
    return code


def decode(cryptCode, keyCode, num):
    code = []
    k = 0
    for i in range(len(cryptCode)):
        p = (cryptCode[i] - keyCode[k % len(keyCode)] + num) % num
        k += 1
        code.append(p)
    return code


def menu(word, key, dictionary, num):
    print()
    print('Меню.')
    print('1. Выбор алфавита (латинский или русский).')
    print('2. Ввод строки.')
    print('3. Настройка шифрующего алгоритма (ввод ключа).')
    print('4. Шифрование строки, используя шифр Виженера.')
    print('5. Расшифровывание строки.')
    try:
        choice = float(input('Выбор: '))
    except ValueError:
        print('Нужно ввести число от 1 до 5!')
        menu(word, key, dictionary, num)
    if choice < 1 or choice > 5:
        print('Неверный выбор. Нужно ввести цифру от 1 до 4.'
              'Попробуйте снова!\n')
        menu(word, key, dictionary, num)
    elif choice == 1:
        dictionary, num = dict_choice()
        menu(word, key, dictionary, num)
    elif choice == 2:
        print('Введите строку для шифрования:')
        word = input()
        menu(word, key, dictionary, num)
    elif choice == 3:
        print('Введите ключ шифрования:')
        key = input()
        menu(word, key, dictionary, num)
    elif choice == 4:
        if word != '' and key != '' and dictionary != {}:
            try:
                wordCode = encode_value(word, dictionary)
                keyCode = encode_value(key, dictionary)
                cryptCode = encode(wordCode, keyCode, num)
                crypt = decode_word(cryptCode, dictionary)
                print('Строка для шифрования:', word)
                print('Ключ шифрования:', key)
                if crypt != '':
                    print('Зашифрованная строка:', crypt)
                else:
                    print('Выбран алфавит, который не совпадает с алфавитом строки!')
            except ZeroDivisionError:
                print('Выбран алфавит, который не совпадает с алфавитом строки!')
        elif word == '':
            print('Вы не ввели строку!')
        elif key == '':
            print('Вы не ввели ключ шифрования!')
        elif dictionary == {}:
            print('Вы не выбрали алфавит!')
        menu(word, key, dictionary, num)
    elif choice == 5:
        if word != '' and key != '' and dictionary != {}:
            try:
                cryptCode = encode_value(word, dictionary)
                keyCode = encode_value(key, dictionary)
                wordDecode = decode(cryptCode, keyCode, num)
                wordDec = decode_word(wordDecode, dictionary)
                print('Строка для расшифрования:', word)
                print('Ключ шифрования:', key)
                if wordDec != '':
                    print('Расшифрованная строка:', wordDec)
                else:
                    print('Выбран алфавит, который не совпадает с алфавитом строки!')
            except ZeroDivisionError:
                print('Выбран алфавит, который не совпадает с алфавитом строки!')
        elif word == '':
            print('Вы не ввели строку!')
        elif key == '':
            print('Вы не ввели ключ шифрования!')
        elif dictionary == {}:
            print('Вы не выбрали алфавит!')
        menu(word, key, dictionary, num)


wordStart = ''
keyStart = ''
dictionaryStart = {}
numStart = 0
menu(wordStart, keyStart, dictionaryStart, numStart)