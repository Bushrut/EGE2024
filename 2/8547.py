
print('X','Y','Z','W')
case = [0,1]

for x in case:
    for y in case:
        for z in case:
            for w in case:
                if (not x or not y) and (w <= (not x)) and ((w and (not x) or z or (not y))):
                    print(x,y,z,w)