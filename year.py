a = int(input())
n = int(input())
b = a + n
if a < 0 and b >= 0:
    b += 1
elif a > 0 and b <= 0:
    b -= 1
print(b)