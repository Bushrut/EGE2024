summ_n = 0
min_n = 10001
for n in range(4, 10000):
    s = '5' + '2'*n
    while '72' in s or '522' in s or '2222' in s:
        s = s.replace('72', '2', 1)
        s = s.replace('522', '27', 1)
        s = s.replace('2222', '5', 1)
    summ_n = sum(map(int,s))
    if summ_n == 63:
        min_n = min(n, min_n)
print(min_n)