def r(s,f):
    if s == f:
        return 1
    if s> f :
        return 0
    return r(s+1,f) + r(s+2,f) + r(s+3,f)
print(r(0,8) + r(0,9) + r(0,10))