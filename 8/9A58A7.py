start = 100000
finish = 999999
count = 0
for i in range(start, finish +1):
    line = str(i)
    set_l = set(line)
    if len(set_l) == 6 and int(line[0])%2 == 0 and int(line[2])%2 == 0 and int(line[4])%2 == 0 and int(line[1])%2 != 0 and int(line[3])%2 != 0 and int(line[5])%2 != 0:
        count+=1
    if len(set_l) == 6 and int(line[0])%2 != 0 and int(line[2])%2 != 0 and int(line[4])%2 != 0 and int(line[1])%2 == 0 and int(line[3])%2 == 0 and int(line[5])%2 == 0:
        count+=1
print(count)