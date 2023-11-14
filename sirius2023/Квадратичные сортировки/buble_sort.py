a = [8, 1, 7, 4, 3, 9, 2, 5, 6, 10]
n = len(a)
unordered = True
count = 0
while unordered:
    unordered = False
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            unordered = True
    n -= 1
    count += 1
print(count)
