# case = [0, 1, 2, 1]
# ls = [int(input()) for x in range(3)]
# flg = True
# count = 0
# while flg:
#     for ligth in case:
#         if ls[ligth] == 0:
#             flg = False
#             break
#         ls[ligth] = ls[ligth] - 1
#         count += 1
# print(count)

a = int(input())
b = int(input())
c = int(input())
print(min(4 * a, 2 * b + 1, 4 * c + 2))