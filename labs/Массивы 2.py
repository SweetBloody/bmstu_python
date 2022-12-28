#Пользователь вводит количество элементов массива и диапозон случайных чисел
# для заполнения массива A. В массиве А поменять местами максимальный и
# минимальный элементы и вывести измененный массив. Из данного массива
# разложить отрицательные и положительные элементы по двум массивам.
# Вывести количество элементов массива, которые больше ср. арифм.(для массива
# с положительными числами), и количество элементов, которые меньше ср. арифм.
# (для массива с отрицательными числами)
import random as rn

#Ввод данных и создание массива
N = int(input('Введите количество элементов массива:'))
a,b = map(int,input('Введите диапозон случайных чисел через пробел:').split())
if b < a:
    a,b = b,a
A = []
for i in range(N):
    x = rn.randint(a, b)
    A.append(x)
print('Массив', A)

#меняем местами макс и мин элементы
minA = A[0]
maxA = minA
imaxA = 0
iminA = 0
for i in range(len(A)):
    if A[i] > maxA:
        maxA = A[i]
        imaxA = i
    if A[i] < minA:
        minA = A[i]
        iminA = i
A[iminA], A[imaxA] = A[imaxA], A[iminA]
print('Измененный массив А:', A)

#Генерация массивов из положит. и отриц. элементов + сред. арифм.
Otr = []
Pol = []
SOtr = 0
kOtr = 0
SPol = 0
kPol = 0
for x in A:
    if x < 0:
        Otr.append(x)
        SOtr += x
        kOtr += 1
    if x > 0:
        Pol.append(x)
        SPol += x
        kPol += 1
print('----------------------------------')
if kOtr != 0:
    SOtr = SOtr / kOtr
    kOtr = 0
    for x in Otr:
        if x < SOtr:
            kOtr +=1
    print('Массив отрицательных чисел (Otr):', Otr)
    print('Среднее арифметическое массива Otr:', '{:7.3f}'.format(SOtr))
    print('Количество элементов меньших сред. арифм. массива Otr:', kOtr)
else:
    print('Нет отрицательных элементов')
print()
print('----------------------------------')
if kPol != 0:
    SPol = SPol / kPol
    kPol = 0
    for x in Pol:
        if x > SPol:
            kPol +=1
    print('Массив положительных чисел (Pol):', Pol)
    print('Среднее арифметическое массива Pol:', '{:7.3f}'.format(SPol))
    print('Количество элементов больших сред. арифм. массива Pol:', kPol)
else:
    print('Нет положительных элементов')
