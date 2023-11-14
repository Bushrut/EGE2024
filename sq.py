n = int(input())
m = int(input())
if n > m:
    n, m = m, n
if n % 2 == 1:
    print(m - n + 1 )
else:
    print(2 * (m - n + 2) )
