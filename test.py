start = 123
finish = 2023
res = 0
count = 1
for i in range(start,finish+1,2):
    if count %2 != 0:
        res -= 2
    else:
        res += 2
    count += 1
print(res)