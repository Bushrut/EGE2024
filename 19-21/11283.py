def f(s,s2, m):
    if s + s2 >= 342: return m%2==0
    if m == 0: return 0
    h = [f(s+2, s2, m-1), f(s*5, s2, m-1), f(s, s2+2, m-1), f(s, s2*5, m-1)]
    return any(h) if m%2!=0 else all(h) # меняем all на any в 19 задаче
print(19, min(s for s in range(1, 326) if f(11,s, 2)))
print(20, [s for s in range(1, 326) if not f(11,s, 1) and f(11,s, 3)][:2])
print(21, min(s for s in range(1, 326) if not f(11,s, 2) and f(11,s, 4)))