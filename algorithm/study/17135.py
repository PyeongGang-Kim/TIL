import sys
from collections import deque
'''
%%
문제를 잘못읽었음.
문제를 먼저 이해부터 하고 들어가자


각 적들에 인덱싱을 하고
각 궁수를 배치 할 수 있는 부분들에서 bfs를 하면서 우선순위를 찾아 기록
궁수를 3가지 위치에 배정

이미 제거된 적을 담을 셋
이번에 제거할 적을 담을 셋

우선순위순서로 찾고 이미 제거된 적이 아닐 경우 해당인덱스 기록 & 이번에 제거할 적을 담을 셋에 기록

1. 궁수 3 배치하는 방법들.

'''
def bfs():
    for i in range(M):
        vl = [[False for _ in range(N)] for _ in range(M)]
        vl[N-1][i] = True
        Q.append([i, N-1, -D])
        if nl[N-1][i]:
            el[i].append([nl[N-1][i], 1])


        xl, xh = max(0, i-1), min(M, i+2)
        while Q:
            x, y, dis = Q.popleft()
            for dx, dy in d:
                tx, ty = x + dx, y + dy
                if xl <= tx < xh and 0 <= ty < N and not vl[ty][tx]:
                    vl[ty][tx] = True
                    Q.append([tx, ty, dis+1])
                    if nl[ty][tx]:
                        el[i].append([nl[ty][tx], dis+1])
            if len(el[i]) == cnt+1:
                Q.clear()
                break


def comb(c = 3, arr = [], dep = 0):
    global r
    if r == cnt:
        return
    if not c:
        solve(arr)
        return
    for i in range(dep, N-c+1):
        arr.append(i)
        comb(c-1, arr, i+1)
        arr.pop()


def solve(arr):
    global r
    defeated = set()
    time = 0
    ac = 0
    while 1:
        time += 1
        temp_defeated = set()
        for i in range(3):
            for j in range(len(el[i])):
                if el[arr[i]][j][0] not in defeated and el[arr[i]][j][1] <= time:
                    temp_defeated.add(el[arr[i]][j][0])
                    break
        ac += len(temp_defeated)
        defeated = defeated.union(temp_defeated)
        for i, n in enumerate(el2):
            if n == time:
                defeated.add(i)
        if len(defeated) == cnt:
            r = max(r, ac)
            return




d = [[-1, 0], [0, -1], [1, 0]]
N, M, D = map(int, sys.stdin.readline().split())
Q = deque()
el = [[] for _ in range(M)]
nl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 적에게 번호 매겨 주기.
cnt = 0
el2 = []
for j in range(N):
    for i in range(M):
        if nl[j][i]:
            cnt += 1
            nl[j][i] = cnt
            el2.append(N-j)
if not cnt:
    print(0)
else:
    bfs()
    r = 0
    comb()
    print(r)