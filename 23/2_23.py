# +1
# +4
# *2
# 4 - > 28 содержит 11 и не содержит 18

def r(s,f):
    if s == 18:
        return 0
    if s > f:
        return 0
    if s == f:
        return 1
    return r(s+1,f) + r(s+4,f) + r(s*2,f)

print(r(4,11)*r(11,28))