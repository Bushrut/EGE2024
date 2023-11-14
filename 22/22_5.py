import csv

with open('22_10596.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    ttw = [0] * 13
    fail = 0
    for row in data:
        dep = row[2].split(';')
        if int(row[0]) < max([int(i) for i in dep]):
            fail += 1
        max_time = max([(ttw[int(i)]) for i in dep])
        ttw[int(row[0])] = max_time + int(row[1])
    ttw.pop(0)
    print(ttw)
    print('Максимальное время:', max(ttw))
    print('Минимальное время:', min(ttw))
    print('Количество фейлов:', fail)

