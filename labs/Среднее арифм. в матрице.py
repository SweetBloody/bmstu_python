from math import exp

N = int(input('Введите размер массивов G и A: \n'))

#Задаем все массивы
R = [0] * N
MN = [0] * N
B = [[0] * N for i in range (N)]

#Ввод исходных массивов
lenG = -1
lenA = -1
while lenG != N:
    print('Введите элементы массива G через пробел:')
    G = list(map(float, input().split()))
    lenG = len(G)
    if lenG != N:
        print('Необходимо {} чисел!'.format(N))
        print()
while lenA != N:
    print('Введите элементы массива A через пробел:')
    A = list(map(float, input().split()))
    lenA = len(A)
    if lenA != N:
        print('Необходимо {} чисел!'.format(N))
        print()
print()
#Составление массива B и нахождение ср. арифм.
for i in range(N):
    for j in range(N):
        B[j][i] = exp((G[j] * A[i]))
        R[i] = R[i] + B[j][i]
for i in range(N):
    R[i] = R[i] / N

#Нахождение количества элементов меньших ср. арифм.
for k in range (N):
    for i in range (N):
        if B[i][k] < R[k]:
            MN[k] += 1

#Вывод
print('Матрица B:')
for i in range (N):
    for j in range (N):
        if (B[i][j] > 10**(-5) and B[i][j] < 10**5)\
           or (B[i][j] < -10**(-5) and B[i][j] > -10**5):
            print('{:7.3f}'.format(B[i][j]), end = '    ')
        else:
            print('{:7.3e}'.format(B[i][j]), end = '    ')
    print()
print()
print('Массив R (среднее арифметическое элементов по столбцам):')
for i in range (N):
    if (R[i] > 10**(-5) and R[i] < 10**5)\
       or (R[i] < -10**(-5) and R[i] > -10**5):
        print('{:7.3f}'.format(R[i]), end = '    ')
    else:
        print('{:7.3e}'.format(R[i]), end = '    ')
print()
print()
print('Массив MN (кол-во элементов меньших ср.арифм. по столбцам): \n', *MN)
            
