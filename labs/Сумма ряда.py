nmax = int(input('Введите максимальное итераций: '))
x = float(input('Введите значение x:'))
eps = float(input('Введите значение eps :'))
step = float(input('Введите значение шага печати суммы:'))
stepi = step
k = 3
t = x ** k
i = 1
s = 0
while abs(t / k) > eps:
    # проверка, что было не больше nmax итераций
    if i > nmax:
        print('Не удалось найти сумму ряда с выбранной точностью')
        break
    s += t / k
    t = t * x * x
    k += 2
    if i == stepi:
        if s > 10 ** (-5) and s < 10 ** 5:
            print('Шаг:', stepi, 'Сумма:', '{:7.3f}'.format(s))
        else:
            print('Шаг:', stepi, 'Сумма:', '{:7.3e}'.format(s))
        stepi += step
    i += 1 # увеличение счетчика итераций
if s > 10 ** (-5) and s < 10 ** 5:
        print('Значение суммы равно:', '{:7.3f}'.format(s))
else:
        print('Значение суммы равно:', '{:7.3e}'.format(s))


