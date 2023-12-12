def f(x,y):
    return (4*x + y < a) or (x < y) or (22<=x)

for a in range(200):
    if all(f(x,y) for x in range(200) for y in range(200)):
        print(a)
        break

