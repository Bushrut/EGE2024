import csv

def r(s,k):
    c = 0
    for i in range(8):
        if s.count(s[i]) == k:
            c += 1
    return c

with open('/home/user/Документы/ЕГЭ/доп_2024/ЕГЭ. Информатика. Типовые экзаменационные варианты. 20 вариантов/9/9 вариант 2.csv','r') as csvfile:
    counter = 0
    data = csv.reader(csvfile, delimiter=';')
    for row in data:
        row = row[:8]
        if r(row,2) == 6:
            mn = min(map(int, row))
            if row.count(str(mn)) == 1:
                counter+=1

    print(counter)