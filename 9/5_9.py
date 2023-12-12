import csv

with open('/home/user/Документы/ЕГЭ/доп_2024/ЕГЭ. Информатика. Типовые экзаменационные варианты. 20 вариантов/9/9 варианты 5-8.csv','r') as csvfile:
    counter = 0
    data = csv.reader(csvfile, delimiter=';')
    for row in data:
        mn = max(map(int,row))
        sn = sum(map(int,row)) - mn
        ln = list(map(int,row))
        if mn < 2* sn and (max(ln) + min(ln) == (sum(ln) - max(ln) + min(ln))):
            counter+=1
        
    print(counter)