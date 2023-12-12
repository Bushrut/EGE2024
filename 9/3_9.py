import csv

def r(s,k):
    c = 0
    for i in range(8):
        if s.count(s[i]) == k:
            c += 1
    return c

with open('/home/user/Документы/ЕГЭ/доп_2024/ЕГЭ. Информатика. Типовые экзаменационные варианты. 20 вариантов/9/9 вариант 3.csv','r') as csvfile:
    counter = 0
    data = csv.reader(csvfile, delimiter=';')
    for row in data:
        row = row[:8]
        if r(row,3) == 3 and r(row,2) == 2:
            nr = sum(int(i) for i in row if row.count(i) == 1)
            rp3 = max(int(i) for i in row if row.count(i) == 3)
            if nr/3 <= rp3:
                counter+=1

    print(counter)