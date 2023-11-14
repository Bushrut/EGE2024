N = int(input())
M = int(input())
S = int(input())
P = int(input())
t = 0
for i in range(N):
    if i == N - 1:
        t += M * 60 + S
        break
    t += M * 60 + S + P
print(t // 60)
print(t % 60)
