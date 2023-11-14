n = int(input())
count = 0
s1 = []
# for i in range(1, n + 1):
#     x = bin(i)
#     x = x[2:]
#     if i % 2 == 0:
#         z = sum([int(z) for z in x])
#         if z % 2 == 0:
#             count += 1
# print(count)
for i in range(n):
    s1.append(i)
print(s1)
print(s1[:-3])
print(s1[-3:])
print(s1[:3])


