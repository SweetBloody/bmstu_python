string = 'привет пока мама машина кисель fff абвгдежзик'
print(string)
arr = string.split()
arr_new = []
for word in arr:
    flag = True
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                flag = False
                break
    if flag:
        arr_new.append(word)

print('Слова, состоящие из неповторяющихся символов:')
for word in arr_new:
    print(word, end=' ')
