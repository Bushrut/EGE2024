
print('X','Y','Z','W')
case = [0,1]

for x in case:
    for y in case:
        for z in case:
            for w in case:
                if (((x or y) == (y <= z)) or w ) == False:
                    print(x,y,z,w)