r = {1:1, 2:2}

for n in range(3, 36):
    if n %2 == 0:
        r[n] = 3*(n-1) + r[n-1] + 5
    else:
        r[n] = 3*(n+1) + r[n-2] - 2
    
print(r[35])