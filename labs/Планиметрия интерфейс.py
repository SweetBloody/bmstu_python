from tkinter import *
from tkinter import font as tkFont
from math import sqrt

coordinates = []


# Функция нахождения координат для построения прямой
def line_coords(x1, y1, x2, y2):
    if x1 == x2:
        return x1, 0, x2, 400

    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2

    y1 = b
    y2 = k * 470 + b

    return 0, y1, 470, y2


# Функция определения координаты точки пересечения двух прямых
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return "null", "null"

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


# Функция создания массива точек пересечения
def intersection_array():
    global coordinates

    inter_lines = []
    intersect = []
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            x, y = line_intersection(coordinates[i], coordinates[j])

            if x != "null" and y != "null" and\
                    x >= 0 and x <= 470 and y >= 0 and y <= 400:
                intersect.append([x, y])
                inter_lines.append([i, j])

    return intersect, inter_lines


# Функция нахождения длины отрезка
def length(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Функция проверки нахождения 3-ех точек на одной прямой
def line_check(point1, point2, point3):
    eps_k = 0.05
    eps_b = 1

    if point1[0] == point2[0] == point3[0]:
        return 1

    if point1[0] == point2[0]:
        k1 = 1
        b1 = point1[0]
    else:
        k1 = (point1[1] - point2[1]) / (point1[0] - point2[0])
        b1 = point2[1] - k1 * point2[0]

    if point2[0] == point3[0]:
        k2 = 1
        b2 = point2[0]
    else:
        k2 = (point2[1] - point3[1]) / (point2[0] - point3[0])
        b2 = point3[1] - k2 * point3[0]

    if point1[0] == point3[0]:
        k3 = 1
        b3 = point3[0]
    else:
        k3 = (point1[1] - point3[1]) / (point1[0] - point3[0])
        b3 = point3[1] - k3 * point3[0]

    if abs(k1 - k2) <= eps_k and abs(k3 - k2) <= eps_k and abs(k1 - k3) <= eps_k and\
        abs(b1 - b2) <= eps_b and abs(b3 - b2) <= eps_b and abs(b1 - b3) <= eps_b:
        return 1
    else:
        return 0


# Функция нахождения площади треугольника
def triangle_square(point1, point2, point3):
    if line_check(point1, point2, point3) == 1:
        return "null"

    l1 = length(point1[0], point1[1], point2[0], point2[1])
    l2 = length(point2[0], point2[1], point3[0], point3[1])
    l3 = length(point1[0], point1[1], point3[0], point3[1])

    p = (l1 + l2 + l3) / 2
    s = sqrt(p * (p - l1) * (p - l2) * (p - l3))

    return s


# Функция проверки точек пересечения
def inter_point_check(point1, point2, point3):
    flag = [0, 0, 0]

    if point1[0] == point2[0] or point1[0] == point2[1] or \
            point1[0] == point3[0] or point1[0] == point3[1]:
        flag[0] = 1

    if point1[1] == point2[0] or point1[1] == point2[1] or \
            point1[1] == point3[0] or point1[1] == point3[1]:
        flag[1] = 1

    if point2[0] == point3[0] or point2[0] == point3[1]:
        flag[2] = 1

    if point2[1] == point3[0] or point2[1] == point3[1]:
        flag[2] = 1

    if flag[0] == 1 and flag[1] == 1 and flag[2] == 1:
        return 1
    else:
        return 0


# Функция нахождения треугольника минимальной площади
def min_triangle(intersect, inter_lines):
    s = 100000000000
    point1, point2, point3 = "null", "null", "null"

    for i in range(len(intersect) - 2):
        for j in range(i + 1, len(intersect) - 1):
            for k in range(j + 1, len(intersect)):
                if triangle_square(intersect[i], intersect[j], intersect[k]) != "null":
                    if triangle_square(intersect[i], intersect[j], intersect[k]) < s\
                            and inter_point_check(inter_lines[i], inter_lines[j], inter_lines[k]) == 1:
                        s = triangle_square(intersect[i], intersect[j], intersect[k])
                        point1 = intersect[i]
                        point2 = intersect[j]
                        point3 = intersect[k]

    return point1, point2, point3


# Функция отрисовки треугольника
def draw_triangle(point1, point2, point3):
    points = [point1[0], point1[1],
              point2[0], point2[1],
              point3[0], point3[1]]

    canvas.create_polygon(points, outline='black', fill='red', width=2)


# Функция вывода ошибки "Нет треугольника"
def warning():
    warn = Label(window, font=helv14, text='Нет треугольника', justify=RIGHT, bg="#8C8FEF")
    warn.grid(row=5, column=0, columnspan=4)


# Функция вывода сообщения об успешной работе
def ok():
    ok = Label(window, font=helv14, text='Наименьший треугольник', justify=RIGHT, bg="#8C8FEF")
    ok.grid(row=5, column=0, columnspan=4)

# Функция вывода сообщения об ошибке ввода
def error():
    error = Label(window, font=helv14, text='Ошибка ввода', justify=RIGHT, bg="#8C8FEF")
    error.grid(row=5, column=0, columnspan=4)


# -------------------------------------- Интерфейс --------------------------------------

# Кнопка добавления прямой
def add_btn():
    global coordinates

    try:
        x_1, y_1, x_2, y_2 = line_coords(int(x1.get()), int(y1.get()),
                                     int(x2.get()), int(y2.get()))
        canvas.create_line(x_1, y_1, x_2, y_2)
        line = [[x_1, y_1], [x_2, y_2]]
        coordinates.append(line)
        x1.delete(0, END)
        y1.delete(0, END)
        x2.delete(0, END)
        y2.delete(0, END)

    except Exception:
        error()




# Кнопка завершения ввода
def stop_btn():
    intersect, inter_lines = intersection_array()

    if len(intersect) < 3:
        warning()
    else:
        point1, point2, point3 = min_triangle(intersect, inter_lines)
        if point1 == "null" and point2 == "null" and point3 == "null":
            warning()
        else:
            draw_triangle(point1, point2, point3)
            ok()





window = Tk()
window.title("Планиметрия")
canvas = Canvas(window, width=470, height=400, bg='white')
canvas.grid(row=4, column=0, columnspan=4)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
width = width // 2 - 190
height = height // 2 - 210
window.geometry('485x630+{}+{}'.format(width, height))
window.resizable(width=False, height=False)
helv14 = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)
helv16 = tkFont.Font(family='Helvetica', size=16)

# Надписи
coords = Label(window, font=helv16, text='Введите координаты двух точек:', bg="#8C8FEF")
coords.grid(row=0, column=0, columnspan=4, pady=(10, 5), padx=(80, 80))

# Ввод координат
x1_lbl = Label(window, font=helv14, text='x1:', justify=RIGHT, bg="#8C8FEF")
x1_lbl.grid(row=1, column=0)

x1 = Entry(window, font=helv14, width=8)
x1.grid(row=1, column=1, pady=(10, 10), padx=(10, 10))


y1_lbl = Label(window, font=helv14, text='y1:', justify=RIGHT, bg="#8C8FEF")
y1_lbl.grid(row=2, column=0)

y1 = Entry(window, font=helv14, width=8)
y1.grid(row=2, column=1, pady=(10,10), padx=(10, 10))


x2_lbl = Label(window, font=helv14, text='x2:', justify=RIGHT, bg="#8C8FEF")
x2_lbl.grid(row=1, column=2)

x2 = Entry(window, font=helv14, width=8)
x2.grid(row=1, column=3, pady=(10,10), padx=(10, 10))


y2_lbl = Label(window, font=helv14, text='y2:', justify=RIGHT, bg="#8C8FEF")
y2_lbl.grid(row=2, column=2)

y2 = Entry(window, font=helv14, width=8)
y2.grid(row=2, column=3, pady=(10,10), padx=(10, 10))

# Кнопки
add = Button(window, text="Добавить прямую", bg="#6A6ECD", fg="#262A89",
               width=15, height=1, font=helv14, command=add_btn)

add.grid(row=3, column=0, columnspan=2, pady=(10, 10))


stop = Button(window, text="Закончить ввод", bg="#6A6ECD", fg="#262A89",
               width=15, height=1, font=helv14, command=stop_btn)

stop.grid(row=3, column=2, columnspan=2, pady=(10, 10))

window.config(bg="#8C8FEF")
window.mainloop()
