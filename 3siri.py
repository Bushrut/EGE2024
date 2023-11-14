n = int(input())
t = n//2
max_n = (t)*2
min_n = (t)*1
mid_n = (max_n+min_n)//2
if mid_n >= n:
    print(t)
else:
    print(t+1)