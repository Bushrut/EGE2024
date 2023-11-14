# Дан массив a1,a2,…an. Необходимо выбрать в нём два элемента ai и aj такие, что i<j, и отношение aj/ai максимально и больше 1
# Входные данные
# В первой строке задано целое число 2≤n≤100 000 — количество элементов в массиве.
# Во второй строке заданы n целых положительных чисел ai(1≤i≤n,1≤ai≤5000)
# Выходные данные
# Выведите два числа — индексы элементов i и j. Если ответов несколько, то выведите любой из них.
# Если ответа нет, то выведите два нуля, разделённых пробелом.
n = int(input())
a = list(map(int, input().split()))
idx_i_best = 0
idx_j_best = 1
idx_i_min = 0
for j in range(2, len(a)):
    if a[j - 1] < a[idx_i_min]:
        idx_i_min = j - 1
    if a[j] / a[idx_i_min] > a[idx_j_best] / a[idx_i_best]:
        idx_j_best = j
        idx_i_best = idx_i_min

if a[idx_j_best] / a[idx_i_best] > 1:
    print(idx_i_best + 1, idx_j_best + 1)
else:
    print(0,0)