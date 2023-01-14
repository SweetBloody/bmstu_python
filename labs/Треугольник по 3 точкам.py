#Косарев ИУ7-11Б
#Определение длин сторон треугольника по заданным координатам.
#Найти высоту, проведенную из наибольшего угла треугольника.
#Определить, является ли треугольник прямоугольным.
#Ввести координаты одной точки (int) и определить, находится
# ли она внутри треугольника или нет.
#Если находится внутри треугольника, то найти расстояние от этой
# точки до наиболее удаленной стороны или ее продолжения.

#Ввод данных
from math import sqrt
xA,yA = map(int,input('Введите координаты точки А:').split())
xB,yB = map(int,input('Введите координаты точки B:').split())
xC,yC = map(int,input('Введите координаты точки C:').split())

#Длины сторон, существует ли треугольник
AB=sqrt((xA - xB) ** 2 + (yA - yB) ** 2)
BC=sqrt((xB - xC) ** 2 + (yB - yC) ** 2)
AC=sqrt((xA - xC) ** 2 + (yA - yC) ** 2)
g=[AB,BC,AC]
max = -1
for i in range (3):
    if g[i] > max:
        max = g[i]
        
if max == AB:
    p = BC
    q = AC
if max == BC:
    p = AB
    q = AC
if max == AC:
    p = BC
    q = AB
if p + q <= max:
    print('Треугольника не существует')
else:


    #Вывод длин
    print('AB =','{:7.4f}'.format(AB))
    print('BC =','{:7.4f}'.format(BC))
    print('AC =','{:7.4f}'.format(AC))

    #Определение наибольшего угла
    if max == AB:
        print('Наибольший угол - ACB')
    if max == BC:
        print('Наибольший угол - BAC')
    if max == AC:
        print('Наибольший угол - ABC')

    #Нахождение высоты
    p = (AB + BC + AC) / 2
    S = sqrt(p * (p - AC) * (p - BC) * (p - AC))
    H = 2 * S / max
    print('Высота, проведенная из наибольшего угла равна','{:7.4f}'.format(H))

    #Определение прямоугольного треугольника
    c = (xA - xB) ** 2 + (yA - yB) ** 2
    a = (xB - xC) ** 2 + (yB - yC) ** 2
    b = (xA - xC) ** 2 + (yA - yC) ** 2
    if a + b == c or a + c == b or b + c == a:
        print('Треугольник прямоугольный')
    else:
        print('Треугольник непрямоугольный')

    #Ввод координат точки. Находится ли в треугольнике
    xT,yT = map(int,input('Введите координаты точки: ').split())
    prATB = (xA - xT) * (yB - yT) - (yA - yT) * (xB - xT) #векторы TA и TB
    prBTC = (xB - xT) * (yC - yT) - (yB - yT) * (xC - xT) #векторы TB и TC
    prATC = (xC - xT) * (yA - yT) - (yC - yT) * (xA - xT) #векторы TA и TC
    if prATB != 0:
        signATB = prATB / abs(prATB)
    else:
        signATB = 0
    if prBTC != 0:
        signBTC = prBTC / abs(prBTC)
    else:
        signBTC = 0
    if prATC != 0:
        signATC = prATC / abs(prATC)
    else:
        signATC = 0
    u1 = signATB == 0 and signBTC==signATC
    u2 = signBTC == 0 and signATC==signATB
    u3 = signATC == 0 and signBTC==signATB
    if signATB == signBTC == signATC:
        print('Данная точка находится в треугольнике')
        flag = 1
    elif u1 == True or u2 == True or u3 == True:
        print('Данная точка лежит на стороне треугольника')
        flag = 1
    else:
        print('Данная точка не находится в треугольнике')
        flag = 0

    #Расстояние от данной точки до наиболее удаленной стороны
    if flag == 1:
        L = [0] * 3
        L[0] = abs(prATB) / AB
        L[1] = abs(prBTC) / BC
        L[2] = abs(prATC) / AC
        max = L[0]
        for i in range(3):
            if L[i] > max:
                max = L[i]
        if max == L[0]:
            print('Наибольшее расстояние-до стороны AB:', '{:7.4f}'.format(max))
        if max == L[1]:
            print('Наибольшее расстояние-до стороны BC:', '{:7.4f}'.format(max))
        if max == L[2]:
            print('Наибольшее расстояние-до стороны AC:', '{:7.4f}'.format(max))




