count = 0
for n in range(1, 101):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        count += 1
print(count)
