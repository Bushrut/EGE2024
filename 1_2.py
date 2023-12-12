a, b, n, m = [int(input()) for i in range(4)]
nm = n*m
r = 0
c = 0
for i in range(1, nm):
    c += 1
    r += i
    if r == nm:
        break
c = a * c + (c-1) * b
print(c)