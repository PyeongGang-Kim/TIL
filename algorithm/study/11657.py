import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ml = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    ml[s].append([e, d])
vl = [0xfffffff for _ in range(N+1)]
vl[1] = 0
for i in range(N-1):
    for j in range(1, N+1):
        for idx, d in ml[j]:
            if vl[j] != 0xfffffff and vl[idx] > vl[j] + d:
                vl[idx] = vl[j] + d

chk = False
for j in range(1, N+1):
    for idx, d in ml[j]:
        if vl[j] != 0xfffffff and vl[idx] > vl[j] + d:
            chk = True
            break

r = []
if chk:
    r.append('-1')
else:
    for i in range(2, N+1):
        if vl[i] != 0xfffffff:
            print(str(vl[i]))
        else:
            print('-1')
print('\n'.join(r))