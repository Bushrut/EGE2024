a = int(input())
r1 = int(input())
r2 = int(input())

x = int((r1**2 - r2**2 + a**2)/(2*a))
y = int(((r2**2) - (a-x)**2)**(1/2))

print(x)
print(-y)

