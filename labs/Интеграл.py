from math import sin, cos

# Функция
def f(x):
    f = sin(x) ** 3 * cos(x)
    return(f)

# Первообразная
def F(x):
    F = sin(x) ** 4 / 4
    return(F)

# Правые прямоугольники
def square(a, b, n):
    Integ = 0
    step = (b - a) / n
    x = a + step
    for i in range(n+1):
        Integ = Integ + f(x)
        x += step
    Integ = Integ * step
    return(Integ)

# Метод Симпсона
def simpson(a, b, n):
    Integ = f(a)
    step = (b - a) / n
    for i in range(1, n // 2 + 1):
        x = a + 2 * i * step
        Integ = Integ + 2 * f(x) + 4 * f(x - step)
    Integ = (Integ - f(b)) * step / 3
    return(Integ)

# Ввод данных
start = float(input('Введите начальное значение аргумента: \n'))
stop = float(input('Введите конечное значение аргумента: \n'))
N1 = int(input('Введите первое количество разбиений: \n'))
N2 = int(input('Введите второе количество разбиений: \n'))

# Таблица
Integ_sq_1 = square(start, stop, N1)
Integ_sq_2 = square(start, stop, N2)
Integ_simp_1 = simpson(start, stop, N1)
Integ_simp_2 = simpson(start, stop, N2)
print('│', '—' * 19, '│', '—' * 15, '│', '—' * 15, '│', sep='')
print('│', ' ' * 7, 'Метод', ' ' * 7, '│', ' ' * 3, 'N1 ={:5d}'.format(N1), ' ' * 3, '│',
      ' ' * 3, 'N2 ={:5d}'.format(N2), ' ' * 3, '│', sep='')
print('│', '—' * 19, '│', '—' * 15, '│', '—' * 15, '│', sep='')
print('│', '  Правых прямоуг.  ', '│', ' ', '{:13.8f}'.format(Integ_sq_1),
      ' ', '│', ' ', '{:13.8f}'.format(Integ_sq_2), ' ', '│', sep='')
print('│', '—' * 19, '│', '—' * 15, '│', '—' * 15, '│', sep='')
print('│', '     Симпсона      ', '│', ' ', '{:13.8f}'.format(Integ_simp_1),
      ' ', '│', ' ', '{:13.8f}'.format(Integ_simp_2), ' ', '│', sep='')
print('│', '—' * 19, '│', '—' * 15, '│', '—' * 15, '│', sep='')

IntegT = F(stop) - F(start) # Точное значение интеграла
print('Точное значение интеграла:\n {:8.8f}'.format(IntegT))

# Правые прямоугольники ошибки
print('—' * 20)
print('Метод правых прямоугольников. Ошибки.')
Abs_Mis_sq1 = abs(IntegT - Integ_sq_1)
Abs_Mis_sq2 = abs(IntegT - Integ_sq_2)
if Abs_Mis_sq1 < Abs_Mis_sq2:
    Abs_Mis_sq = Abs_Mis_sq1
else:
    Abs_Mis_sq = Abs_Mis_sq2
Otn_Mis_sq = abs(Abs_Mis_sq / IntegT)
print('Абсолютная ошибка:\n {:10.8f}'.format(Abs_Mis_sq))
print('Относительная ошибка:\n {:10.8f}'.format(Otn_Mis_sq))

# Метод Симпсона ошибки
print('—' * 20)
print('Метод Симпсона. Ошибки.')
Abs_Mis_simp1 = abs(IntegT - Integ_simp_1)
Abs_Mis_simp2 = abs(IntegT - Integ_simp_2)
if Abs_Mis_simp1 < Abs_Mis_simp2:
    Abs_Mis_simp = Abs_Mis_simp1
else:
    Abs_Mis_simp = Abs_Mis_simp2
Otn_Mis_simp = abs(Abs_Mis_simp / IntegT)
print('Абсолютная ошибка:\n {:10.8f}'.format(Abs_Mis_simp))
print('Относительная ошибка:\n {:10.8f}'.format(Otn_Mis_simp))

# Менее точный метод
print('—' * 20)
if Abs_Mis_sq >= Abs_Mis_simp:
    print('Менее точный метод - метод правых треугольников')
    flag = 1
else:
    print('Менее точный метод - метод Симпсона')
    flag = 2

# Считаем значение интеграла с точностью Eps
Eps = float(input('Введите значение точности: \n'))
n = 10
if flag == 1:
    Integ_2n = square(start, stop, 2 * n)
    Integ_n = square(start, stop, n)
    while abs(Integ_2n - Integ_n) > Eps:
        n = n * 2
        Integ_n = Integ_2n
        Integ_2n = square(start, stop, 2 * n)
    print('Значение интеграла с заданной точностью Eps = {}: \n'.format(Eps),
          '{:8.8f}'.format(Integ_2n))
    print('Количество разбиений = ', n)
if flag == 2:
    Integ_2n = simpson(start, stop, 2 * n)
    Integ_n = simpson(start, stop, n)
    while abs(Integ_2n - Integ_n) > Eps:
        n = n * 2
        Integ_n = Integ_2n
        Integ_2n = simpson(start, stop, 2 * n)
    print('Значение интеграла с заданной точностью Eps = {}: \n'.format(Eps),
          '{:8.8f}'.format(Integ_2n))
    print('Количество разбиений = ', n)