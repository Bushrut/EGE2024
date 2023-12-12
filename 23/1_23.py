# +1
# +4
# *2
# 3 - > 24 не содержит 11 и 17

def r(s,f):
    if s == 11 or s == 17:
        return 0
    if s == f:
        return 1
    if s > f:
        return 0
    return r(s+1,f) + r(s+4,f) + r(s*2,f)

print(r(3,24))