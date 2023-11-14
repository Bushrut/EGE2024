# (x \/ ¬y) /\ ¬(y ≡ z) /\ ¬w,
print('X','Y','Z','W')
case = [0,1]

for x in case:
    for y in case:
        for z in case:
            for w in case:
                if not (not(w <= x) or (y <= z) or not y):
                    print(x,y,z,w)