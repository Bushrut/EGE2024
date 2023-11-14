nums = [i for i in range(10, 1000001)]
count = 0
for n in nums:
    n_str = str(n)
    x = list(n_str)
    res_x = 0
    for k in x:
        res_x += int(k) ** (len(x))
    if n == res_x:
        count += n
        print(n)
print(count)
