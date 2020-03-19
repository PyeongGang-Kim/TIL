import sys
from collections import deque
'''
cnt에는 치즈가 있는 좌표의 갯수를 저장해 둔다.

제일 밖에 한 점에서 bfs를 하면서 1(치즈가 있는 부분)을 만나면 그 좌표를 저장해 둔다.
저장한 좌표들의 갯수가 cnt와 같으면 종료한다.
다르면 cnt를 좌표들의 갯수만큼 빼 주고 해당 좌표에 존재하는 치즈를 0으로 바궈 준다.
비짓 리스트를 초기화하고 반복한다. 
'''

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
nl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
vl = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
for j in range(N):
    for i in range(M):
        if nl[j][i]:
            cnt += 1
if not cnt:
    print(0)
    print(0)
else:

    minx, miny, maxx, maxy = 0, 0, M, N
    time = 0
    while cnt:
        time += 1
        Q = deque([(minx, miny)])
        vl[miny][minx] = True
        ml = []
        while Q:
            x, y = Q.popleft()
            for dx, dy in d:
                tx, ty = x + dx, y + dy
                if minx <= tx < maxx and miny <= ty < maxy and not vl[ty][tx]:
                    vl[ty][tx] = True
                    if nl[ty][tx]:
                        ml.append((tx, ty))
                    else:
                        Q.append((tx, ty))
        if cnt == len(ml):
            print(time)
            print(len(ml))
            break
        else:
            cnt -= len(ml)
            minx, maxx = maxx, minx
            miny, maxy = maxy, miny
            for tx, ty in ml:
                nl[ty][tx] = 0
                minx = min(minx, tx-1)
                maxx = max(maxx, tx+1)
                miny = min(miny, ty-1)
                maxy = max(maxy, ty+1)
            for j in range(miny, maxy):
                for i in range(minx, maxx):
                    vl[j][i] = False
