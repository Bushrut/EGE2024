# n = 27
# print('Canonical', (n-1+4)//5)
# print('My resolve', (n-7)//5+2)

# for n in range(7, 10000, 1):
#     can = (n-1+4)//5
#     m_res = (n-7)//5+2
#     if can != m_res:
#         print("fail", n)


n = int(input())
f = [float("inf")] * (n + 1)
f[1] = 0
for i in range(2, n + 1):
    f[i] = min(f[i - 2], f[i - 3]) + 1
k = [float("inf")] * (n + 1)
k[n] = 0
for i in range(n - 1, 0, -1):
    k[i] = min(k[i + 1], k[i + 2]) + 1
ans = -1
for i in range(1, n + 1):
    if f[i] == k[i]:
        ans = f[i]
        break
print(ans)