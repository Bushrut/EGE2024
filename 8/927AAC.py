n = ['А', 'В', 'О', 'Р', 'Т']
count = 0
for s1 in n:
    for s2 in n:
        for s3 in n:
            for s4 in n:
                for s5 in n:
                    for s6 in n:
                        line = s1 + s2 + s3 + s4 + s5 + s6
                        count = count + 1
                        if 'ВОРОТА' == line:
                            print(line)
                            print(count)
                            break