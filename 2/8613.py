
print('X','Y','Z','W')
case = [0,1]

for x in case:
    for y in case:
        for z in case:
            for w in case:
                if (not x or y or not z or w) and not(not x or w):
                    print(x,y,z,w)