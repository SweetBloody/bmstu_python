B = []
GL = ['a', 'e', 'i', 'o', 'u']
M = int(input('Введите количество строк и стобцов (1 число): \n'))
for i in range(M):
    print('Введите {} строку матрицы через пробел:'.format(i+1))
    B.append(input().split())
k = 0
s = len(GL)
zv_num = 0
for i in range(s):
    for p in range(M):
        for m in range(M):
            if GL[i] == B[p][m]:
                k += 1
    if k != 1:
        GL[i] = '*'
        zv_num += 1
    k = 0
for i in range (zv_num):
    GL.remove('*')
print('Массив:')
for i in range(M):
    for j in range(M):
        print(B[i][j], end = '  ')
    print()
print('Массив гласных:\n', GL)

