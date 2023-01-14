B = []
GL = ['a','e','i','o','u']
M = int(input('Введите количество строк и стобцов (1 число): \n'))
for i in range (M):
    print('Введите {} строку матрицы через пробел:'.format (i+1))
    B.append(input().split())
k = 0
del_num = 0
s = len(GL)
for i in range (s):
    print(GL[i-del_num])
    for y in B:
        if GL[i-del_num] == y:
            k += 1
    if k != 1:
        GL.remove(GL[i-del_num])
        del_num += 1
    k = 0
print(B)
print(GL)

