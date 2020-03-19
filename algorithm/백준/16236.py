import sys
'''
먹을 수 있는 먹이가 있으면 계속 진행한다.
Q에서 꺼낸 거리가 달라지는 순간마다 해당 거리에 먹이가 있는지 확인한 후
먹이가 있으면 가장 위, 왼쪽에 있는 먹이를 먹는다.
size가 커지는지 확인한다.
그리고 먹이까지의 거리 di를 혼자 활동한 시간 r에 더해준다.

먹이를 먹을 때마다 다시 초기화 해주고 bfs를 해야 한다.


%%%%
더 이상 갈 곳이 없음에도 불구하고 먹을 수 있는 먹이가 없으면 멈춰야 한다.

'''
N = int(sys.stdin.readline())
size_list = [0 for i in range(7)]
nl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

flcnt = 0
for j in range(N):
    for i in range(N):
        if nl[j][i]:
            if nl[j][i] == 9:
                sx, sy = i, j
                nl[j][i] = 0
            else:
                flcnt += 1
                size_list[nl[j][i]] += 1

shark_size = 2
cnt = 0
time = 0
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while flcnt:
    min_size = 6
    tmpsize = min(shark_size, 6)
    for i in range(tmpsize):
        if size_list[i]:
            min_size = i
            break
    if min_size >= shark_size:
        break
    else:
        Q = [(sx, sy, 0)]
        vl = [[False for _ in range(N)] for _ in range(N)]
        vl[sy][sx] = True
        fl2 = []
        tmpd = 0
        while Q:
            x, y, dis = Q.pop(0)
            if dis != tmpd:
                if fl2:
                    tmpx, tmpy = fl2[0]
                    for tx, ty in fl2:
                        if ty < tmpy:
                            tmpx, tmpy = tx, ty
                        elif ty == tmpy:
                            if tx < tmpx:
                                tmpx = tx
                    size_list[nl[tmpy][tmpx]] -= 1
                    nl[tmpy][tmpx] = 0
                    sx, sy = tmpx, tmpy
                    cnt += 1
                    flcnt -= 1
                    if cnt == shark_size:
                        shark_size += 1
                        cnt = 0
                    time += dis
                    break
                tmpd = dis
            for tx, ty in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
                if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx] and nl[ty][tx] <= shark_size:
                    vl[ty][tx] = True
                    Q.append((tx, ty, dis+1))
                    if 0 < nl[ty][tx] < shark_size:
                        fl2.append((tx, ty))
        if fl2:
            continue
        else:
            break

print(time)
