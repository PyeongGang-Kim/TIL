import sys
from collections import deque
import heapq
'''
섬을 확인한다
각 섬을 인덱싱하고 섬간 거리를 입력한 간선 리스트를 만든다.

MST 이용한다.
'''
def bfs(x, y, idx):
    Q = deque([(x, y)])
    vl[y][x] = idx
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < M and 0 <= ty < N and ml[ty][tx] and not vl[ty][tx]:
                Q.append((tx, ty))
                vl[ty][tx] = idx

def mkb(x, y):
    global il
    ci = vl[y][x]
    for dx, dy in d:
        tx, ty = x + dx, y + dy
        if 0 <= tx < M and 0 <= ty < N and not ml[ty][tx]:
            while 1:
                tx, ty = tx + dx, ty + dy
                if 0 <= tx < M and 0 <= ty < N:
                    if ml[ty][tx]:
                        dist = abs(x-tx) + abs(y-ty)
                        if dist > 2:
                            Map[ci][vl[ty][tx]] = min(Map[ci][vl[ty][tx]], dist-1)
                        break
                else:
                    break

def unionfind(x):
    if union[x]:
        tmp = unionfind(union[x])
        union[x] = tmp
        return tmp
    return x


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, M = map(int, sys.stdin.readline().split())
maxd = N * M
ml = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
vl = [[0 for _ in range(M)] for _ in range(N)]
idx = 1
for j in range(N):
    for i in range(M):
        if ml[j][i] and not vl[j][i]:
            bfs(i, j, idx)
            idx += 1

Map = [[maxd for _ in range(idx+1)] for _ in range(idx+1)]

for j in range(N):
    for i in range(M):
        if ml[j][i]:
            mkb(i, j)

il = []
for j in range(1, idx+1):
    for i in range(1, idx+1):
        if Map[j][i] != maxd:
            il.append([Map[j][i], j, i])
il.sort(reverse=True)

union = [0 for _ in range(idx)]
r = 0
cnt = 2
while il:
    dist, il1, il2 = il.pop()
    t1 = unionfind(il1)
    t2 = unionfind(il2)
    if t1 != t2:
        union[t2] = t1
        r += dist
        cnt += 1
        if cnt == idx:
            break


if cnt == idx:
    print(r)
else:
    print(-1)