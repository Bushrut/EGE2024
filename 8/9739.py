n = sorted(['М', 'А', 'Н', 'Г', 'У', 'С', 'Т',])
count = 0
for s1 in n:
    for s2 in n:
        for s3 in n:
            for s4 in n:
                for s5 in n:
                    for s6 in n:
                        line = s1 + s2 + s3 + s4 + s5 + s6
                        count +=1
                        if line[0] != 'У' and line.count('М') == 2 and line.count('Г') <= 1:
                            print(line, count)
a = 7*8*8*4*1
b = 7*8*4*1*4
c = 7*4*1*4*8
d = 3*1*4*8*8
e = 1*4*8*8*8
print(a+b+c+d+e)