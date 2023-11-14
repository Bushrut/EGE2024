n = int(input())
m = int(input())
k = int(input())
c = int(input())
counter = 0
if (n*m)%k == 0:
    counter = int((n*m)/k)
else:
    t = (n*m)%k
    print("остаток от деления", t)
    if t >= c:
        counter = int(n*m//k +1)
    else:
        counter = int(n*m//k)
print(counter)
