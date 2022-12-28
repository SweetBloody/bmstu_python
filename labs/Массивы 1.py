#В одномерном массиве найти сумму элементов, находящихся между максимальным и
# минимальным значениями данного массива + создать новый массив B из этих
# элементов (сами максимальный и минимальный элементы в сумму и массив
# не включать). В массиве B поменять местами первый и последний элементы,
# второй и предпоследний элементы и т. д.. Также найти в массиве B
# среднее арифметическое всех четных элементов, стоящих на нечетных местах, и
# ср. арифм. всех нечетных стоящих на четных местах.
# *Пользователь вводит количество элементов массива и диапозон случайных чисел
# для заполнения массива A
import random as rn

#Ввод данных и создание массива
N = int(input('Введите количество элементов массива:'))
if N > 0:
    a,b = map(int,input('Введите диапозон случ. чисел через пробел:').split())
    if b < a:
        a,b = b,a
    A = []
    for i in range(N):
        x = rn.randint(a, b)
        A.append(x)
    print('Массив', A)

    #Нахождение минимального и максимального элемента
    maxA = A[0]
    minA = maxA
    minNum = 0
    maxNum = 0
    for i in range (N):
        if A[i] > maxA:
            maxA = A[i]
            maxNum = i
        if A[i] < minA:
            minA = A[i]
            minNum = i
    print('Минимальное значение:', minA)
    print('Максимальное значение:', maxA)
    if minNum < maxNum:
        p = minNum
        q = maxNum
    else:
        p = maxNum
        q = minNum

    #Создание нового массива и нахождение суммы его элементов
    S = 0
    B = []
    for i in range (p+1,q):
        S += A[i]
        B.append(A[i])
    print('Массив B из элементов между макс. и мин. элементами массива А:', B)
    print('Сумма элементов массива B:', S)
    for i in range (len(B) // 2):
        B[i],B[len(B) - i - 1] = B[len(B) - i - 1],B[i]
    print('Измененный массив B:', B)

    #Нахождение средних арифметических
    SRch = 0
    kch = 0
    SRnch = 0
    knch = 0
    for i in range (1,len(B),2):
        if B[i] % 2 == 0:
            SRch += B[i]
            kch += 1
    for i in range (0,len(B),2):
        if B[i] % 2 != 0:
            SRnch += B[i]
            knch += 1
    if kch == 0:
        print('В массиве нет подходящих четных элементов')
    else:
        SRch = SRch / kch
        print('Среднее арифметическое четных:', '{:7.3f}'.format(SRch))
    if knch == 0:
        print('В массиве нет подходящих нечетных элементов')
    else:
        SRnch = SRnch / knch
        print('Среднее арифметическое нечетных:', '{:7.3f}'.format(SRnch))
else:
    print('Количество должно быть больше нуля!')
