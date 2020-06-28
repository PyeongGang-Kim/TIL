'''
행복도
앞에서부터 최소값 뒤에서부터 최대값
피로도
앞에서부터 최대값 뒤에서부터 최소값
0인경우는 무조건 가장 좋은 경우의 수로 변경
'''
import sys
input = sys.stdin.readline
N = int(input())
nl = [[*map(int, input().split())] for _ in range(N)]
hmin = [0] * N
hmax = [0] * N
pmax = [0] * N
pmin = [0] * N
inf = 10**9+1
hmin[0] = nl[0][0] if nl[0][0] else inf
pmax[0] = nl[0][1] if nl[0][1] else 0
for i in range(1, N):
    if nl[i][0]:
        hmin[i] = min(hmin[i-1], nl[i][0])
    else:
        hmin[i] = hmin[i-1]
    if nl[i][1]:
        pmax[i] = max(pmax[i-1], nl[i][1])
    else:
        pmax[i] = pmax[i-1]

hmax[-1] = nl[-1][0] if nl[-1][0] else 0
pmin[-1] = nl[-1][1] if nl[-1][1] else inf
for i in range(N-2, -1, -1):
    if nl[i][0]:
        hmax[i] = max(hmax[i+1], nl[i][0])
    else:
        hmax[i] = hmax[i+1]
    if nl[i][1]:
        pmin[i] = min(pmin[i+1], nl[i][1])
    else:
        pmin[i] = pmin[i+1]
chk = False
for i in range(N-2, -1, -1):
    if hmax[i+1] < hmin[i]:
        if pmax[i] < pmin[i+1]:
            chk = True
            result = i + 1
            break
if not chk:
    print(-1)
else:
    print(result)