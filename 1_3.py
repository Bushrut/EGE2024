m = int(input())
r = []
for i in range(m):
    a, b = map(int, input().split())
    r.append(sum(int(1/n*100000) for n in range(a,b+1))) 
for i in range(m):
    print(r[i])
