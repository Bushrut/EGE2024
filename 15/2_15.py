def f(x,y):
    return (x*x + y*y > 128) or (y < -x + a)

for a in range(100):
    if all(f(x,y) for x in range(100) for y in range(100)):
        print(a)
        break