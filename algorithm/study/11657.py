T = int(input())
for t in range(1, T+1):
    N = int(input())
    ml = [list(map(int, input().split())) for _ in range(N)]
    R = 0
    for i in range(N):
        vl = [0xffffffff for _ in range(N)]
        vl[i] = 0
        for i in range(N-1):
            for j in range(N):
                for idx in range(N):
                    if ml[j][idx] and vl[j] != 0xffffffff and vl[idx] > vl[j]+ml[j][idx]:
                        vl[idx] = vl[j] + ml[j][idx]

        for k in range(N):
            if vl[k] == 0xffffffff:
                vl[k] = -10000
        print(vl)
        R = max(R, max(vl))
    print(R)

#
#
#
# N, M = map(int, input().split())
# ml = [[] for _ in range(N+1)]
# for _ in range(M):
#     s, e, d = map(int, input().split())
#     ml[s].append([e, d])
# vl = [0xfffffff for _ in range(N+1)]
# vl[1] = 0
# for i in range(N-1):
#     for j in range(1, N+1):
#         for idx, d in ml[j]:
#             if vl[j] != 0xfffffff and vl[idx] > vl[j] + d:
#                 vl[idx] = vl[j] + d
#
# chk = False
# for j in range(1, N+1):
#     for idx, d in ml[j]:
#         if vl[j] != 0xfffffff and vl[idx] > vl[j] + d:
#             chk = True
#             break
#
# r = []
# if chk:
#     r.append('-1')
# else:
#     for i in range(2, N+1):
#         if vl[i] != 0xfffffff:
#             print(str(vl[i]))
#         else:
#             print('-1')
# print('\n'.join(r))