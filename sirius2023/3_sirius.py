n = 12
n_max = 0
count = 0
for _ in range(8):
    str_n = str(n)
    f = str_n[0]
    s = str_n[-1]
    n = n + int(s) - int(f)
    if n > n_max:
        n_max = n
    if n % 10 == 0:
        count += 1
print(n)
print('count', count)
print('max',n_max)