a, b, c = input().split()
a = int(a)
b = int(b)
res = 0
if c == '+':
    res = a + b
if c == '-':
    res = max(a-b, b-a)
if c == '*':
    res = a*b
if c == '/':
    if a != 0 and b != 0:
        res = max(a//b, b//a)
if c == '^':
    res = max(a**b, b**a)
print(res)