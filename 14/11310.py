# 4MxF​+265AFDNx​+N4x931B3L​+NGx4F​+FKJB5xIK

for x in "0123456789ABCDEFGHIJKLMN":
    n = int("4M" + x + "F",24) + int('265AFDN' + x,24) + int('N4' + x + '931B3L',24) + int('NG' + x + '4F',24) + int('FKJB5' + x + 'IK',24)

    if n % 23 == 0:
        print(x, n//23)