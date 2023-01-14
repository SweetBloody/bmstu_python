# функция выравнивания по правому краю
def right_side(text):
    maxLen = 0
    for i in range(len(text)):
        if len(text[i]) > maxLen:
            maxLen = len(text[i])
    for i in range(len(text)):
        k = maxLen - len(text[i])
        print(' ' * k, text[i], sep='')


# функция выравнивания по ширине
def width_text(text):
    maxLen = 0
    wideText = [x for x in text]
    for i in range(len(wideText)):
        if len(wideText[i]) > maxLen:
            maxLen = len(wideText[i])
    for i in range(len(wideText)):
        num = 0
        delta = maxLen - len(wideText[i])
        for j in range(len(wideText[i])):
            if wideText[i][j] == ' ':
                num += 1
        if delta >= num and len(wideText[i]) != maxLen and num != 0:
            k = delta // num
            extra = delta - num * k
            flag = 1
            m = 0
            for j in range(len(wideText[i])):
                if m < len(wideText[i]) and wideText[i][m] == ' ':
                    if flag <= extra:
                        wideText[i] = wideText[i][:m] + ' ' * (k + 1)\
                                      + wideText[i][m:]
                        m += k + 1
                        flag += 1
                    else:
                        wideText[i] = wideText[i][:m] + ' ' * k\
                                      + wideText[i][m:]
                        m += k
                m += 1
        elif num == 0:
            print(wideText[i])
        else:
            number = 0
            m = 0
            for j in range(len(wideText[i])):
                if m < len(wideText[i]) and wideText[i][m] == ' ' and number < delta:
                    wideText[i] = wideText[i][:m] + ' ' + wideText[i][m:]
                    m += 1
                    number += 1
                m += 1
    return wideText


# функция удаления слова
def word_delete(text):
    word = input('Введите слово, которое хотите удалить:\n')
    if word != '':
        L = len(word)
        flag = 0
        for i in range(len(text)):
            for j in range(len(text[i]) - L + 1):
                if text[i][j:(j + L)] == word:
                    text[i] = text[i][:j] + text[i][(j + L + 1):]
                    flag = 1
                    break
            if flag == 1:
                break
    else:
        print('Вы не ввели слово!')
        word_delete(text)
    return text

# функция замены слова
def word_replace(text):
    wordDel = input('Введите слово, которое хотите заменить:\n')
    L = len(wordDel)
    wordRep = input('Введите слово, на которое хотите заменить'
                    ' слово, записанное выше:\n')
    if wordRep != '' or wordDel != '':
        for i in range(len(text)):
            for j in range(len(text[i]) - L + 1):
                if text[i][j:(j + L)] == wordDel:
                    text[i] = text[i][:j] + wordRep + text[i][(j + L):]
    else:
        print('Вы не ввели слово!')
        word_replace(text)
    return text


# функция нахождения арифметического примера
def find_sum(text):
    sum = ''
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == '0' or text[i][j] == '1' or text[i][j] == '2' or\
            text[i][j] == '3' or text[i][j] == '4' or text[i][j] == '5' or\
            text[i][j] == '6' or text[i][j] == '7' or text[i][j] == '8' or\
            text[i][j] == '9':
                str = i
                start = j
                sum = text[i][j]
                break
    for i in range(start + 1, len(text[str])):
        if text[str][i] == '0' or text[str][i] == '1' or text[str][i] == '2'\
        or text[str][i] == '3' or text[str][i] == '4' or text[str][i] == '5'\
        or text[str][i] == '6' or text[str][i] == '7' or text[str][i] == '8'\
        or text[str][i] == '9' or text[str][i] == '-' or text[str][i] == '+'\
        or text[str][i] == '*' or text[str][i] == '/' or text[str][i] == '('\
        or text[str][i] == ')' or text[str][i] == ' ':
            sum = sum[:] + text[str][i]
        else:
            break
    if text[str][start - 1] == '(':
        sum = '(' + sum[:]
    if text[str][start - 1] == '-' and text[str][start - 2] == '(':
        sum = '(-' + sum[:]
    finalSum = ''
    for i in range(len(sum)):
        if sum[i] != ' ':
            finalSum = finalSum[:] + sum[i]
    return finalSum, str


# калькулятор
def number(id, sum):
    result = ''
    flag = 0
    if sum[id] == '(':
        id += 1
        result, id = addition(id, sum)
        id += 1
    else:
        while id < len(sum):
            if sum[id] == '-' and flag != 1:
                result = '-'
                id += 1
                flag = 1
            elif sum[id] != '*' and sum[id] != '/' and sum[id] != '+' and sum[id] != '-' and sum[id] != ')' and sum[id] != '(':
                result += sum[id]
                id += 1
                flag = 1
            else:
                break
    if result == '-':
        result, id = number(id, sum)
        result = -1 * result
        return result, id
    else:
        result = float(result)
        return result, id


def multiplication(id, sum):
    result, id = number(id, sum)
    while id < len(sum) and (sum[id] == '*' or sum[id] == '/'):
        if sum[id] == '*':
            id += 1
            a, id = number(id, sum)
            result *= a
        else:
            id += 1
            a, id = number(id, sum)
            result /= a
    return result, id


def addition(id, sum):
    result, id = multiplication(id, sum)
    while id < len(sum) and (sum[id] == '+' or sum[id] == '-'):
        if sum[id] == '+':
            id += 1
            a, id = multiplication(id, sum)
            result += a
        else:
            id += 1
            a, id = multiplication(id, sum)
            result -= a
    return result, id


# нахождение предложений с одинаковым кол-вом слов
def equal_sentences(text):
    string = ''
    for x in text:
        string += x + ' '
    sentence = []
    a = ''
    for i in range(len(string)):
        if string[i] == ' ' and a == '':
            pass
        elif string[i] != '.':
            a = a + string[i]
        else:
            a = a + string[i]
            sentence.append(a)
            a = ''
    sent = [''] * len(sentence)
    for i in range(len(sentence)):
        sent[i] = sentence[i]
    flag = 0
    for i in range(len(sent)):
        start = 0
        for j in range(len(sent[i])):
            if sent[i][j] == '/' or sent[i][j] == '*' or\
                (sent[i][j] == '-' and sent[i][j+1] == ' ')\
                    or sent[i][j] == '+':
                a = a + sent[i][start:j + 1]
                start = j + 2
                flag = 1
        if flag == 1:
            sent[i] = a + sent[i][start:len(sent[i])]
            flag = 0
        a = ''
    for i in range(len(sent)):
        amount = len(sent[i].split())
        if amount != 0:
            print('Предложения с {} словами:'.format(amount))
            print(sentence[i])
            sent[i] = ''
            for j in range(i+1, len(sent)):
                num = len(sent[j].split())
                if amount == num:
                    print(sentence[j])
                    sent[j] = ''






def menu(text):
    print('Меню')
    print('1. Выравнивание текста по левому краю.')
    print('2. Выравнивание текста по правому краю.')
    print('3. Выравнивание текста по ширине.')
    print('4. Удаление заданного слова.')
    print('5. Замена одного слова другим во всем тексте.')
    print('6. Вычисление арифметического выражения.')
    print('7. Найти и напечатать предложения, в которых количество слов'
          ' совпадает.')
    print('8. Выход')
    try:
        choice = int(input('Выберите пункт меню:\n'))
    except ValueError:
        print('Нужно ввести число от 1 до 8!')
        menu(text)
    if choice < 1 or choice > 8:
        print('Неверный выбор. Нужно ввести цифру от 1 до 8.'
              'Попробуйте снова!')
        menu(text)
    elif choice == 1:
        for x in text:
            print(x)
        print()
        menu(text)
    elif choice == 2:
        right_side(text)
        print()
        menu(text)
    elif choice == 3:
        text_wide = width_text(text)
        for x in text_wide:
            print(x)
        print()
        menu(text)
    elif choice == 4:
        text_del = word_delete(text)
        for x in text_del:
            print(x)
        print()
        menu(text)
    elif choice == 5:
        text_replace = word_replace(text)
        for x in text_replace:
            print(x)
        print()
        menu(text)
    elif choice == 6:
        id = 0
        sum, h = find_sum(text)
        number, id = addition(id, sum)
        print(sum, '=', number)
        print()
        menu(text)
    elif choice == 7:
        equal_sentences(text)
        print()
        menu(text)
    elif choice == 8:
        pass


text = ['Ему удалось выровнять метлу, но несколько секунд спустя все',
        'повторилось. Казалось, что метла хочет сбросить его. Гарри',
        'понимал, что «Нимбусы (-1 + (  (-3) * 4)) + 5 * (-400)» не принимают',
        'внезапных решений относительно того, чтобы сбросить на землю своего',
        'седока, но тем не менее это происходило. Гарри попробовал',
        'развернуть метлу к своим воротам - в какую-то секунду ему',
        'показалось, что, возможно, стоит крикнуть Вуду чтобы тот взял',
        'тайм-аут. Но тут метла полностью вышла из-под',
        'контроля.']

menu(text)
