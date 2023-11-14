# 47x42696​+8x22
for x in "0123456789ABCDEFGHIJKLMNOPQRS":
    n = int("47" + x + "42696",29) + int('8' + x + '22',29)

    if n % 28 == 0:
        print(x, n//28)