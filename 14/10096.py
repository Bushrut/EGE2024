for x in "0123456789ABCDEFGH":
    n = int("98897" + x + "21",19) + int('2' + x +'923',19)
    if n % 18 == 0:
        print(x, n//18)