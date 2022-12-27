# Сортировки

# Выбором (простым)
def selectionsort(arr):
    for i in range(len(arr)):
        minind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minind]:
                minind = j
        arr[i], arr[minind] = arr[minind], arr[i]
    return arr



# Обменные методы
    # 1) пузырек
def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

    # 2) пузырек с флагом
def bubblesortwithflag(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break
    return arr

    # 3) шейкер
def shakersort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        r_new = left
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                r_new = i
        right = r_new
        l_new = right
        for i in range(right - 1, left - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                l_new = i
        left = l_new
    return arr



# Вставками
    # 1) простыми вставками
def insertionsort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = cur
    return arr

    # 2) вставками с барьером
def insertionsortwithbarrier(arr):
    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[0] = arr[i]
        j = i - 1
        while arr[0] < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = arr[0]
    return arr[1:]

    # 3) вставками с бинарным поиском
def insertionsortwithbinsearch(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        left = 0
        right = i
        while left < right:
            mid = (left + right) // 2
            if cur < arr[mid]:
                right = mid
            else:
                left = mid + 1
        j = i
        while j > left:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[left] = cur
    return arr

    # 4) Шелла
def shellsort(arr):
    step = len(arr) // 2
    while step > 0:
        for i in range(step, len(arr)):
            cur = arr[i]
            j = i - step
            while j >= 0 and cur < arr[j]:
                arr[j + step] = arr[j]
                j = j - step
            arr[j + step] = cur
        step //= 2
    return arr





# Быстрая сортировка
from random import choice

def quicksort(arr):
    if len(arr) > 0:
        mid = choice(arr)
        sred = [i for i in arr if i == mid]
        left = [i for i in arr if i < mid]
        right = [i for i in arr if i > mid]
        return quicksort(left) + sred + quicksort(right)
    else:
        return arr







arr = [4, 8, 2, 5, 9, 1]
print('Простой выбор: ', selectionsort(arr))
print('Пузырек: ', bubblesort(arr))
print('Пузырек с флагом: ', bubblesortwithflag(arr))
print('Шейкер: ', shakersort(arr))
print('Вставка: ', insertionsort(arr))
print('Вставка с барьером: ', insertionsortwithbarrier(arr))
print('Вставка с бинарным поиском: ', insertionsortwithbinsearch(arr))
print('Шелл: ', shellsort(arr))
print('Быстрая сортировка: ', quicksort(arr))