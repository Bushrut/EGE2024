import itertools
n, k = map(int, input().split())
for x in list(itertools.combinations([i for i in range(k)], n)):
    print(*x)