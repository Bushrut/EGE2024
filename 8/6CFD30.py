n = sorted(['Ц', 'А', 'П', 'Л', 'Я'])
count = 0

for s1 in n:
    for s2 in n:
        for s3 in n:
            for s4 in n:
                for s5 in n:
                    line = s1 + s2 + s3 + s4 + s5
                    count+=1
                    if line.count('А') == 1 and line.count('Ц') == 2 and line.count('Л') == 0:
                        print(count)
                        break