count = 0
for x in range(100000, 1_000_000):
    str_x = str(x)
    sum_x = sum(int(i) for i in str_x)
    if sum_x <= 47:
        count += 1
print(count)