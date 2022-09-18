import os

ls = [file for file in os.listdir() if file.endswith(".txt")]
c = ls.sort()
dict1 = {}
len1 = []
for j in ls:
    with open((j), 'rt', encoding='utf8') as f1:
        c = str(len(f1.readlines()))
        len1.append(int(c))
    for i in len1:
        dict1[j] = i
d = sorted(dict1.values())
dict2 = {}
for i in d:
    for k in dict1.keys():
        if dict1[k] == i:
            dict2[k] = dict1[k]
            break
with open('result.txt', 'a', encoding='utf-8') as f:
    for i, j in dict2.items():
        j = str(j)
        f.writelines([i +' ' + '\n',j +' ' + '\n'])
        for m in range(int(j)):
            with open((i), 'rt', encoding='utf8') as f2:
                v = f2.readlines()
                f.writelines(['Строка номер ' + str(m+1), ' файла номер ' + i[0],' ' + v[m] + '\n'])




