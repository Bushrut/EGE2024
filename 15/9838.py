def f(x,y):
    return (x + 2*y > a) or (y < x) or (x < 30)
ma = 0
for a in range(200):
    if all(f(x,y) for x in range(100) for y in range(100)):
        ma = max(ma,a)

print(ma)