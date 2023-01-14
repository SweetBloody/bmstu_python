from tkinter import *
from tkinter import font
import tkinter.messagebox as mb


# ----------------------------------------------- Функции шифрования -----------------------------------------------

# создание словаря
def dictionary():
    dict = {}
    k = 32
    for i in range(0, 95):
        dict[i] = chr(k)
        k += 1
    k = 1040
    for i in range(95, 159):
        dict[i] = chr(k)
        k += 1
    dict[159] = chr(1025)
    dict[160] = chr(1105)
    return dict

dictionary = dictionary()


# преобразуем строку в массив чисел
# каждой букве - свое число
def encode_values(string, dictionary):
    code = []
    for i in range(len(string)):
        for val in dictionary:
            if string[i] == dictionary[val]:
                code.append(val)
    return code


# восстанавливаем строку по массиву чисел
def decode_string(code, dictionary):
    string = ''
    for i in range(len(code)):
        string += dictionary[code[i]]
    return string


# получаем шифр (в виде массива чисел) с помощью ключа
def encode(wordCode, keyCode):
    cryptCode = []
    k = 0
    for i in range(len(wordCode)):
        c = (wordCode[i] + keyCode[k % len(keyCode)]) % 161
        k += 1
        cryptCode.append(c)
    return cryptCode


# расшифровываем шифр (заданный в виде массива чисел) с помощью ключа
def decode(cryptCode, keyCode):
    stringCode = []
    k = 0
    for i in range(len(cryptCode)):
        p = (cryptCode[i] - keyCode[k % len(keyCode)] + 161) % 161
        k += 1
        stringCode.append(p)
    return stringCode


# -------------------------------------------------- Интерфейс ---------------------------------------------------

# Кнопка шифровки
def encode_btn():
    try:
        print_txt.delete(1.0, END)
        wordCode = encode_values(enter_txt.get(1.0, END), dictionary)
        keyCode = encode_values(key_txt.get(), dictionary)
        cryptCode = encode(wordCode, keyCode)
        crypt = decode_string(cryptCode, dictionary)
        print_txt.insert(1.0, crypt)
    except ZeroDivisionError:
        key_warning()


# Кнопка расшифровки
def decode_btn():
    try:
        print_txt.delete(1.0, END)
        cryptCode = encode_values(enter_txt.get(1.0, END), dictionary)
        keyCode = encode_values(key_txt.get(), dictionary)
        wordDecode = decode(cryptCode, keyCode)
        wordDec = decode_string(wordDecode, dictionary)
        print_txt.insert(1.0, wordDec)
    except ZeroDivisionError:
        key_warning()


# Кнопка очистки поля ввода
def enter_del_btn():
    enter_txt.delete(1.0, END)


# Кнопка очистки поля вывода
def print_del_btn():
    print_txt.delete(1.0, END)


# Окно предупреждения о ключе
def key_warning():
    mb.showerror("Ошибка", "Бублик! Ключ введи =)")

# Настройки окна

window = Tk()
window.title('Top secret')
window.resizable(width=False, height=False)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2
h = h // 2
window.geometry('468x480+{}+{}'.format(w - 200, h - 150))

helv15 = font.Font(family='Helvetica', size=15)
helv11 = font.Font(family='Helvetica', size=11)
helv7= font.Font(family='Helvetica', size=8)

# Надписи

lbl_1 = Label(window, text="Поле ввода текста для шифровки/расшифровки:", font=helv15, bg="#000", fg="#aaa")
lbl_1.grid(row=0, column=0, columnspan=4, pady=(10, 10), padx=(5, 5))

lbl_2 = Label(window, text="Результат:", font=helv15, bg="#000", fg="#aaa")
lbl_2.grid(row=5, column=0, columnspan=4, pady=(10, 10), padx=(5, 5))

# Поля ввода/вывода

enter_txt = Text(width=40, height=5, font=helv15, bg="#ccc")
enter_txt.grid(row=1, column=0, columnspan=4, padx=(5, 5))

print_txt = Text(width=40, height=5, font=helv15, bg="#ccc")
print_txt.grid(row=6, column=0, columnspan=4, padx=(5, 5))


# Настройка ключа

key_lbl = Label(window, text="Ключ шифрования:", font=helv11, bg="#000", fg="#aaa")
key_lbl.grid(row=3, column=1, pady=(5, 5), padx=(5, 5))

key_txt = Entry(window, font=helv11, bg="#ccc")
key_txt.grid(row=3, column=2, pady=(5, 5), padx=(5, 5))


# Кнопки шифровки/расшифровки

encode_btn = Button(window, text="Зашифровать", font=helv15, command=encode_btn, bg="#F5DF4D", fg="#555",
                    activebackground="#D3BD2B", activeforeground="#333")
encode_btn.grid(row=4, column=1)

decode_btn = Button(window, text="Расшифровать", font=helv15, command=decode_btn, bg="#F5DF4D", fg="#555",
                    activebackground="#D3BD2B", activeforeground="#333")
decode_btn.grid(row=4, column=2)


# Кнопки очистки

enter_del_btn = Button(window, text="Очистка", font=helv7, command=enter_del_btn, bg="#F5DF4D", fg="#000",
                       activebackground="#D3BD2B", activeforeground="#333")
enter_del_btn.grid(row=2, column=0, columnspan=4, pady=(5, 5), padx=(5, 5))

print_del_btn = Button(window, text="Очистка", font=helv7, command=print_del_btn, bg="#F5DF4D", fg="#000",
                       activebackground="#D3BD2B", activeforeground="#333")
print_del_btn.grid(row=7, column=0, columnspan=4, pady=(5, 5), padx=(5, 5))


window.config(bg="#000")
window.mainloop()


