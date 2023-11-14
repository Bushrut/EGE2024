import csv

with open('/home/user/Документы/ЕГЭ/9/2_9.csv', 'r+') as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    for row in data:
        if row[0] != row[1] != row[2] != row[3] != row[4]:
            print(row)