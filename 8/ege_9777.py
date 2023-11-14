n = sorted(['К', 'О', 'М', 'П', 'Ь', 'Ю', 'Т', 'Е', 'Р'])
count = 0
for s1 in n:
    for s2 in n:
        for s3 in n:
            for s4 in n:
                for s5 in n:
                    line = s1 + s2 + s3 + s4 + s5
                    count +=1
                    if line[0] != 'Ь' and line.count('К') == 2:
                        print(line, count)