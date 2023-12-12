# -1
#  n//2
# 60 - > 2 содержит 10

def r(s,f):
    if s < f:
        return 0
    if s == f:
        return 1
    return r(s-1,f) + r(s//2,f)

print(r(60,10)*r(10,2))