n = sorted(['Л', 'А', 'Й', 'М'])
count = 0

for s1 in n:
    for s2 in n:
        for s3 in n:
            for s4 in n:
                for s5 in n:
                    line = s1 + s2 + s3 + s4 + s5
                    count+=1
                    print(count, line)
                    if count == 922:
                        print(count, line)
                    # if line.count('М') <= 1 :
                    #     print(count)
