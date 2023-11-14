N = int(input())
K = int(input())
a = 1
d = 2
m = 3
flag = True
a_count = N // 2
m_count = N // 3
max_step = 0
if N % 2 == 0:
    max_step = N - 1 + int(N / 2)
else:
    max_step = N + N // 2

win_seq1 = [i for i in range(a, N + 1, 3)]
lose_seq1 = [i for i in range(d, N + 1, 3)]
move_seq = [i for i in range(m, N + 1, 3)]
if N <=3:
    if K == 3:
        print('Yes')
        print(4)
    elif K in win_seq1:
        print('Yes')
        print(K)
    elif K in lose_seq1:
        print('No')
        print(K)
    flag = False
if flag:
    win_seq2 = [i for i in range(a, max_step + 1, 3)]
    lose_seq2 = [i for i in range(d, max_step + 1, 3)]
    move_seq2 = [i for i in range(m, max_step + 1, 3)]

    idx = 0
    if m_count % 2 == 0:
        idx = m_count // 2
        temp = move_seq[:idx]
        win_seq1 = win_seq2[:-idx] + temp[::-1]
        lose_seq1 = lose_seq2[:-idx] + move_seq[idx:]
    else:
        idx = m_count // 2 + 1
        lenWS = idx - (len(win_seq2) - len(win_seq1))
        temp = move_seq[lenWS:idx]
        win_seq1 = win_seq2[:-idx + 1] + temp[::-1]
        lose_seq1 = lose_seq1 + move_seq[:lenWS] + move_seq[idx:]

    if K in win_seq1:
        print('Yes')
        print(win_seq1.index(K) * 3 + 1)
    elif K in lose_seq1:
        print('No')
        print(lose_seq1.index(K) * 3 + 2)

