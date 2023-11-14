n = int(input())
m = int(input())
if (1 + n) * n // 2 < m:
    print(0)
else:
    while m > n:
        print(n)
        m -= n
        n -= 1
print(m)

N = int(input())
M = int(input())

boxes = []
i = N
while i > 0 and M > 0:
    k = min(i, M)
    boxes.append(k)
    M -= k
    i -= 1

if M > 0:
    print("0")
else:
    print(*boxes)