from tkinter import *
from tkinter import font as tkFont
import tkinter.messagebox as box


# Функция информационного окна
def info():
    box.showinfo("Косарев Алексей", "Калькулятор троичной СС")


# Функция полной очистки ввода
def button_c():
    txt.delete(0, END)
    member_txt.delete(0, END)


# Функция удаления последнего символа
def button_del():
    string = txt.get()[:len(txt.get()) - 1]
    txt.delete(0, END)
    txt.insert(0, string)


# Функции кнопок
def button_plus():
    txt.insert(END, "+")


def button_one():
    txt.insert(END, "1")


def button_two():
    txt.insert(END, "2")


def button_minus():
    txt.insert(END, "-")


def button_zero():
    txt.insert(END, "0")


def button_point():
    txt.insert(END, ".")


# Функция кнопки "=" и подсчет значения
def button_equal():
    try:
        member_txt.delete(0, END)
        string = txt.get()+'='
        flag_oper = -1
        flag_minus = 0
        oper_ind = 0
        for i in range(len(txt.get())):
            if txt.get()[i:i + 1] == "+":
                flag_oper = 1
                oper_ind = i
                break
        for i in range(len(txt.get())):
            if txt.get()[i:i + 1] == "-":
                if i == 0:
                    flag_minus = 1
                else:
                    flag_oper = 0
                    oper_ind = i
                    break
        if flag_oper == 0:
            if flag_minus == 0:
                result = to_dec(txt.get()[:oper_ind]) - to_dec(txt.get()[oper_ind + 1:])
            else:
                result = -to_dec(txt.get()[1:oper_ind]) - to_dec(txt.get()[oper_ind + 1:])
        elif flag_oper == 1:
            if flag_minus == 0:
                result = to_dec(txt.get()[:oper_ind]) + to_dec(txt.get()[oper_ind + 1:])
            else:
                result = -to_dec(txt.get()[1:oper_ind]) + to_dec(txt.get()[oper_ind + 1:])
        else:
            if flag_minus == 0:
                result = to_dec(txt.get())
            else:
                result = -to_dec(txt.get())
        txt.delete(0, END)
        member_txt.insert(0, string)
        txt.insert(0, str(to_tern(str(result))))
    except ValueError:
        txt.delete(0, END)
        txt.insert(0, "Incorrect enter")


# Функция перевода из троичной СС в десятичную
def to_dec(number):
    a = list(number.split('.'))
    dec = 0
    
    for i in range(len(a[0])):
        dec += int(a[0][len(a[0]) - 1 - i:len(a[0]) - i]) * 3 ** i
    count = -1

    if len(a) == 2:
        for i in range(len(a[1])):
            dec += float(a[1][i:i + 1]) * 3 ** count
            count -= 1
    return dec


# Функция перевода из десятичной СС в троичную
def to_tern(number):
    a = list(number.split('.'))
    number = float(number)
    try:
        sign = number / abs(number)
    except ZeroDivisionError:
        return 0
    number = abs(number)

    integer = int(number // 1)
    decimal = number % 1

    count = 1
    tern = 0
    while integer > 0:
        tern += integer % 3 * count
        integer //= 3
        count *= 10

    if len(a) == 2:
        max_len = len(a[1])
        index = 1
        count = 0.1
        for i in range(max_len):
            decimal *= 3
            a = decimal // 1
            tern += a * count
            count /= 10
            decimal %= 1
            index += 1
    return tern * sign


# Интерфейс калькулятора

# Параметры окна
window = Tk()
window.title("Калькулятор")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
width = width // 2 - 190
height = height // 2 - 220
window.geometry('385x445+{}+{}'.format(width, height))
window.resizable(width=False, height=False)
helv36 = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD)

# Создание меню
menu = Menu(window)
act_menu = Menu(menu, tearoff=0)
act_menu.add_command(label="+", command=button_plus)
act_menu.add_command(label="-", command=button_minus)
act_menu.add_command(label="=", command=button_equal)

clear_menu = Menu(menu, tearoff=0)
clear_menu.add_command(label="Очистить все", command=button_c)
clear_menu.add_command(label="Удалить символ", command=button_del)

menu.add_cascade(label="Действия", menu=act_menu)
menu.add_cascade(label="Очистить", menu=clear_menu)
menu.add_command(label="Инфо", command=info)

# Создание поля для сохренения примера
member_txt = Entry(window, font=helv36, justify=RIGHT)
member_txt.grid(row=0, column=0, columnspan=3, pady=(10, 2), padx=(10, 10))

# Создание поля ввода примера
txt = Entry(window, font=helv36, justify=RIGHT)
txt.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=(10, 10))


# Создание кнопок

btn_c = Button(window, text="C", bg="#6A6ECD", fg="#262A89",
               width=5, height=2, font=helv36, command=button_c)
btn_c.grid(row=2, column=0)

btn_del = Button(window, text="DEL", bg="#6A6ECD", fg="#262A89",
                 width=5, height=2, font=helv36, command=button_del)
btn_del.grid(row=2, column=1)

btn_plus = Button(window, text="+", bg="#6A6ECD", fg="#262A89",
                  width=5, height=2, font=helv36, command=button_plus)
btn_plus.grid(row=2, column=2)

btn_one = Button(window, text="1", bg="#6A6ECD", fg="#262A89",
                 width=5, height=2, font=helv36, command=button_one)
btn_one.grid(row=3, column=0, pady=(10, 10))

btn_two = Button(window, text="2", bg="#6A6ECD", fg="#262A89",
                 width=5, height=2, font=helv36, command=button_two)
btn_two.grid(row=3, column=1, pady=(10, 10))

btn_minus = Button(window, text="-", bg="#6A6ECD", fg="#262A89",
                   width=5, height=2, font=helv36, command=button_minus)
btn_minus.grid(row=3, column=2, pady=(10, 10))

btn_zero = Button(window, text="0", bg="#6A6ECD", fg="#262A89",
                  width=5, height=2, font=helv36, command=button_zero)
btn_zero.grid(row=4, column=0)

btn_point = Button(window, text=".", bg="#6A6ECD", fg="#262A89",
                   width=5, height=2, font=helv36, command=button_point)
btn_point.grid(row=4, column=1)

btn_equal = Button(window, text="=", bg="#6A6ECD", fg="#262A89",
                   width=5, height=2, font=helv36, command=button_equal)
btn_equal.grid(row=4, column=2)


window.config(bg="#8C8FEF")
window.config(menu=menu)
window.mainloop()

