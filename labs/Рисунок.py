from tkinter import *
from math import sqrt, cos, sin


def f(x, r):
    return sqrt(r * r - x ** 2)



def sun():
    c.create_oval(500, 40, 560, 100,
              fill='#ffff00', outline='#ffff00')

    r1 = 40
    r2 = 60

    for i in range(0, 360, 30):
        rad = i * 3.14 / 180
        x1 = r1 * cos(rad)
        x2 = r2 * cos(rad)
        c.create_line(x1 + 530 , f(x1, r1) + 70,
                      x2 + 530, f(x2, r2) + 70,
                      width=2, fill='#ffff00')
        c.create_line(x1 + 530, -f(x1, r1) + 70,
                      x2 + 530, -f(x2, r2) + 70,
                      width=2, fill='#ffff00')
        
#def sun():
#    x = 590
#
#    for i in range(0, 361, 30):
#        rad = i * 3.14 / 180
#        c.create_line(530, 70,
#                      60 * cos(rad) + 530, 60 * sin(rad) + 70,
#                      width=2, fill='#ffff00')
#
#    c.create_oval(490, 30, 570, 110,
#              fill='#00bfff', outline='#00bfff')
#
#    c.create_oval(500, 40, 560, 100,
#              fill='#ffff00', outline='#ffff00')


        
window = Tk()

c = Canvas(window, width=600, height=550, bg='white')
c.pack()

# море
c.create_rectangle(0, 380, 600, 550,
                   fill='blue', outline='blue')

# небо
c.create_rectangle(0, 380, 600, 0,
                   fill='#00bfff', outline='#00bfff')

# солнце
sun()


# основа корабля
c.create_polygon(70, 335, 510, 335,
                 490, 450, 190, 450,
                 fill='gray', outline='black')

# первый квадрат
c.create_rectangle(500, 335, 390, 225,
                   fill='gray', outline='black')

# второй квадрта
c.create_rectangle(475, 225, 415, 165,
                   fill='gray', outline='black')

# антенна
c.create_rectangle(470, 165, 467, 135,
                  fill='black', outline='black')

# окна второго квадрата
c.create_rectangle(420, 170, 440, 190,
                  fill='white', outline='black')

c.create_rectangle(450, 170, 470, 190,
                  fill='white', outline='black')

c.create_rectangle(420, 200, 440, 220,
                  fill='white', outline='black')

c.create_rectangle(450, 200, 470, 220,
                  fill='white', outline='black')

# дверь первого квадрата
c.create_rectangle(460, 335, 480, 290,
                  fill='black', outline='black')

# контайнеры
c.create_rectangle(110, 335, 220, 315,
                   fill='red', outline='black')

c.create_rectangle(222, 335, 332, 315,
                   fill='green', outline='black')

c.create_rectangle(110, 315, 220, 295,
                   fill='blue', outline='black')

c.create_rectangle(222, 315, 332, 295,
                   fill='blue', outline='black')

c.create_rectangle(222, 295, 332, 275,
                   fill='red', outline='black')

# якорь
c.create_oval(140, 350, 160, 370,
              fill='black', outline='black')

c.create_rectangle(149, 360, 151, 385,
                   fill='black', outline='black')

c.create_line(150, 385, 160, 375,
              width=3)

c.create_line(150, 385, 140, 375,
              width=3)

# иллюминаторы
for i in range(200, 451, 50):
    c.create_oval(i - 5, 355, i + 5, 365,
                  fill='cyan', outline='black')

window.mainloop()

