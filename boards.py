# L = int(input())
# N = int(input())
# boards = [int(input()) for i in range(N)]
#
# count = 0
# i = 0
#
# while i < N:
#     if boards[i] == 0:
#         i += 1
#     else:
#         max_size = min(N - i, L)
#         for j in range(max_size, 0, -1):
#             if all(boards[i:i+j]):
#                 i += j
#                 count += 1
#                 break
#
# print(count)

L = int(input())
N = int(input())
ans = 0
last_start = -10 ** 6
for i in range(N):
    fence_elem = int(input())
    if fence_elem == 1 and i >= last_start + L:
        ans += 1
        last_start = i
print(ans)