# НАЧАЛО
# ПОКА нашлось (52) ИЛИ нашлось (2222) ИЛИ нашлось (1122)
#  ЕСЛИ нашлось (52)
#    ТО заменить (52, 11)
#  КОНЕЦ ЕСЛИ
#  ЕСЛИ нашлось (2222)
#    ТО заменить (2222, 5)
#  КОНЕЦ ЕСЛИ
#  ЕСЛИ нашлось (1122)
#    ТО заменить (1122, 25)
#  КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ

def is_found(k, nm):
    b = k in nm
    return b


for n in range(4,10000):
    num = "5" + "2" * n
    print(n)
    while is_found("52", num) or is_found("2222", num) or is_found("1122", num):
        if is_found("52", num):
            num = num.replace("52", "11", 1)
        if is_found("2222", num):
            num = num.replace("2222", "5", 1)
        if is_found("1122", num):
            num = num.replace("1122", "25", 1)
    if sum(map(int,num)) == 64:
        print(n)
