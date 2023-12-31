# Новый маршрут для трекинга
# Сейчас самое время планировать новые трекинговые маршруты.
# Опишем холмистую местность массивом из n
# чисел. Высота i-го холма равна hi. Маршрут должен идти по k
# подряд идущим холмам (учитывая тот холм, с которого маршрут будет начинаться). Немолодым туристам не очень нравится, когда приходится много раз подниматься в гору — переходить с более низкого холма на более высокий.
# Помогите туристам определиться с выбором маршрута — напишите программу, которая отвечает на запросы о количестве переходов с более низкого холма на более высокий на данном маршруте.
# Входные данные
# В первой строке даны натуральные числа n
# , m (2≤n,m≤2⋅105
# ) — общее количество холмов и количество запросов соответственно.
# Во второй строке даны n
# целых чисел hi(1≤hi≤105)
# — высоты холмов.
# В следующих m
# строках записаны пары чисел lj и rj (1≤li≤rj≤n) — запросы на количество переходов с более низкого холма на более высокий на маршруте с началом в холме lj и завершением в rj
# Выходные данные
# Выведите m
# чисел — ответы на запросы.
# Примеры
# Ввод
# Вывод
# 2 3
# 2 37
# 1 2
# 2 2
# 1 1
# 1
# 0
# 0

n, m = map(int, input().split())
a = list(map(int, input().split()))
l_r_list = []
for i in range(m):
    l, r = map(int, input().split())
    l_r_list.append(l)
    l_r_list.append(r)
p = [0] * n
for i in range(1, n):
    cur_el = a[i]
    last_el = a[i - 1]
    if cur_el > last_el:
        p[i] = p[i - 1] + 1
    else:
        p[i] = p[i - 1]

for j in range(0, m * 2, 2):
    l = l_r_list[j]
    r = l_r_list[j + 1]
    print(p[r-1] - p[l-1])
print(p)
