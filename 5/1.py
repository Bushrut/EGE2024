for n in range(11, 12):
    s = ""
    t = n
    while t > 0:
        s = str(n%4) + s
        t = t//4
    if n % 4 == 0:
        s = s + s[len(s)-2:].zfill(2,0)
    else:
        p = (n % 4) * 2
        s2 = ""
        while p > 0:
            s = str(p%4) + s2
            p = p//4
        s = s + s2
    print(s)

         


