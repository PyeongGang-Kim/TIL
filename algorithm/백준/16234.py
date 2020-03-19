import sys

N, L, R = map(int, sys.stdin.readline().split())
ran = range(N)
nl = [list(map(int, sys.stdin.readline().split())) for _ in ran]
time = 0
Q = []
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
while 1:
    vl = [[False for _ in ran] for _ in ran]
    chk = False
    for j in ran:
        for i in ran:
            if not vl[j][i]:
                vl[j][i] = True
                Q = [[i, j]]
                front = 0
                rear = 1
                tmpsum = nl[j][i]
                while front < rear:
                    x, y = Q[front]
                    front += 1
                    tx, ty = x + 1, y
                    if tx<N and not vl[ty][tx] and L<=abs(nl[y][x] - nl[ty][tx])<=R:
                        Q.append([tx, ty])
                        rear += 1
                        vl[ty][tx] = True
                        tmpsum += nl[ty][tx]
                    tx, ty = x - 1, y
                    if 0<=tx and not vl[ty][tx] and L<=abs(nl[y][x] - nl[ty][tx])<=R:
                        Q.append([tx, ty])
                        rear += 1
                        vl[ty][tx] = True
                        tmpsum += nl[ty][tx]
                    tx, ty = x, y + 1
                    if ty<N and not vl[ty][tx] and L<=abs(nl[y][x] - nl[ty][tx])<=R:
                        Q.append([tx, ty])
                        rear += 1
                        vl[ty][tx] = True
                        tmpsum += nl[ty][tx]
                    tx, ty = x, y - 1
                    if 0<=ty and not vl[ty][tx] and L<=abs(nl[y][x] - nl[ty][tx])<=R:
                        Q.append([tx, ty])
                        rear += 1
                        vl[ty][tx] = True
                        tmpsum += nl[ty][tx]
                if len(Q) > 1:
                    chk = True
                    tmp = tmpsum//len(Q)

                    for i in range(len(Q)):
                        nl[Q[i][1]][Q[i][0]] = tmp
    if not chk:
        break
    time += 1
print(time)