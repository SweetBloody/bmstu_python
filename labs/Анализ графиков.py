import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
import pylab


def func1(x):
    return np.sin(x)


def d_func1(x):
    return - np.sin(x)


def func2(x):
    return 1 / 10 * (x ** 4 / 12 - x ** 3 / 6 - 3 * x ** 2 + 2 * x) - 1


def d_func2(x):
    return 1 / 10 * (x ** 2 - x - 6)


def func3(x):
    return x * x - 3 * x + 1


def d_func3(x):
    return 2


def func4(x):
    return 3 ** x


def d_func4(x):
    return np.log(3) ** 2 * 3 ** x


# Функция нахождения корней
def root(function, a, b, step, mark):
    for i in range(a, b, step):
        try:
            x1 = bisect(function, i, i + 1)
            plt.plot(x1, 0, mark)
        except ValueError:
            pass


# Функция нахождения экстремумов
def extrem(function, x, mark):
    for el in x:
        if function(el) > function(el - 0.1) and function(el) > function(el + 0.1):
            plt.plot(el, function(el), mark)
    for el in x:
        if function(el) < function(el - 0.1) and function(el) < function(el + 0.1):
            plt.plot(el, function(el), mark)

    # minimum = function(-10)
    # for el in x:
    #     if function(el) < minimum:
    #         minimum = function(el)
    # for el in x:
    #     if (abs(function(el) - minimum) <= eps) and (minimum > -5) and (minimum < 5):
    #         plt.plot(el, minimum, mark)


# Функция нахождения точек перегиба
def bend(function, d_function, a, b, step, mark):
    for i in range(a, b, step):
        try:
            x1 = bisect(d_function, i, i + 1)
            plt.plot(x1, function(x1), mark)
        except ValueError:
            pass


x = np.linspace(-10, 10, 200)

plt.plot(x, func1(x), 'r--', label='y = sin(x)')
root(func1, -10, 10, 1, 'r*')
bend(func1, d_func1, -10, 10, 1, 'rs')
extrem(func1, x, 'ro')

plt.plot(x, func2(x), 'b-.', label='y = 0.1 * (x ^ 4 / 12\n - x ^ 3 / 6 - 3 * x ^ 2\n + 2 * x) - 1')
root(func2, -10, 10, 1, 'b*')
bend(func2, d_func2, -10, 10, 1, 'bs')
extrem(func2, x, 'bo')

plt.plot(x, func3(x), 'g', label='y = x^2-3x+1')
root(func3, -10, 10, 1, 'g*')
bend(func3, d_func3, -10, 10, 1, 'gs')
extrem(func3, x, 'go')

plt.plot(x, func4(x), 'y:', label='y = 3^x')
root(func4, -10, 10, 1, 'y*')
bend(func4, d_func4, -10, 10, 1, 'ys')
extrem(func4, x, 'yo')

pylab.text(-9.5, -4.8, "точки - экстремумы\nквадраты - точки перегиба\nзвездочки - корни", fontdict=None)


plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.xlim(-10, 10)
plt.ylim(-5, 5)
plt.legend(loc='upper left')
plt.grid()
plt.show()
