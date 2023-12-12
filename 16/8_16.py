r = dict()
r[1] = 1
r[2] = 1

for n in range(3, 40):
    if n % 2 != 0:
        r[n] = r[n-1] - r[n-2]
    else:
        r[n] = sum(r[i] for i in r)
print(r[39])