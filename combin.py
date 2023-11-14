case = [0, 1]
print(*list('yxwz'), sep='\t')
for x in case:
    for y in case:
        for w in case:
            for z in case:
                if ((x <= y) or (z <= w)) and not (x <= w):
                    print(y, x, w, z, sep='\t')
