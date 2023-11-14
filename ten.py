nums = [i for i in range(500, 601)]
count = 0


def delta(num):
    n_str = str(num)
    num = list(n_str)
    n_dig = []
    for x in num:
        n_dig.append(int(x))
    n_dig.sort(reverse=True)
    maxn = int(str(n_dig[0]) + str(n_dig[1]))
    minn = int(str(n_dig[2]) + str(n_dig[1]))
    return maxn, minn


for n in nums:
    max_num, min_num = delta(n)
    if (max_num - min_num) == 10:
        count += n
print(count)
