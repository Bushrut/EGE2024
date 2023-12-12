r = {1:1}
for n in range(2,13):
    if n %2 != 0:
        r[n] = 3 + r[n-1]*r[n-2] - r[n-1] - r[n-2]
    else:
        r[n] = 2 * r[n-1]
print(r[12])