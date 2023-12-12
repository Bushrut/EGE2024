# A. Прибавить 1
# B. Умножить на 2
# C. Умножить на 3
# 1 - > 25 не содержит 15 и содержит 11

def r(s,f):
    if s == 15:
        return 0
    if s > f:
        return 0
    if s == f:
        return 1
    return r(s+1,f) + r(s*2, f) + r(s*3,f)
print(r(1,11)*r(11,25))