N = int(input())
K = int(input())
res = 0
if N == K:
    res = N
else:
    t = N - 2
    if t % 2 == 0:
        res = int(t/2) + K
    else:
        res = int((N//2) + 1 + K)
print(res)

