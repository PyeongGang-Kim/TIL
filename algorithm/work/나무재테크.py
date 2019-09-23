import sys
sys.stdin = open('asdf.txt')
import collections


def pt(i, j):
    tmp = []
    for k in range(8):
        tx, ty = i + dr[k][0], j + dr[k][1]
        if 0 <= tx < N and 0 <= ty < N:
            nl[ty][tx][1].appendleft(time-1)

dr = [[0, 1], [1, 1], [1, 0], [1, -1], [-1, -1], [-1, 1], [-1, 0], [0, -1]]

N, M, K = map(int, input().split())
nl = [[[5, collections.deque(), i] for i in list(map(int, input().split()))] for _ in range(N)]
tr = [list(map(int, input().split())) for _ in range(M)]
for tree in tr:
    nl[tree[0]-1][tree[1]-1][1].append(-tree[2])
time = 0
while K > time:
    for ny in range(N):
        for nx in range(N):
            if not nl[ny][nx][1]:
                nl[ny][nx][0] += nl[ny][nx][2]
                continue
            tmp = 0
            s = nl[ny][nx][0]
            tmp2 = len(nl[ny][nx][1])
            tmp3 = 0
            i = 0
            while i < tmp2:
                tmp += (time - nl[ny][nx][1][i])
                if tmp > s:
                    break
                i += 1
            tmp4 = 0
            for _ in range(i):
                tmp4 += (time - nl[ny][nx][1][_])
            for _ in range(tmp2 - i):
                tmp3 += (time - nl[ny][nx][1].pop()) // 2
            nl[ny][nx][0] += tmp3 + nl[ny][nx][2] - tmp4
    time += 1
    pts = []

    for ny in range(N):
        for nx in range(N):
            if nl[ny][nx][1]:
                #나무 심어주기 좌표, 나이(time+1)
                for tree in nl[ny][nx][1]:
                    if not (time - tree)%5:
                        pts.append([nx, ny])

    for tree in pts:
        pt(*tree)
cnt = 0
for _ in range(N):
    for __ in range(N):
        cnt += len(nl[_][__][1])
print(cnt)
