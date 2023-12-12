def f(x,y):
    return (x*y<a)or(x<y)or(9<x)

for a in range(100):
    if all(f(x,y) for x in range(100) for y in range(100)):
        print(a)
        break