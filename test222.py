data = [30, 19, 9,35,2,4,1]
res = []
for x in data:
    for y in data:
        t = x + y
        res.append(t)
res.sort()
print(len(res))
for i in range(2,100+1):
    if i not in res:
        print(i)