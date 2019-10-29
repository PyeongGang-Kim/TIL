from collections import deque


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[False for _ in range(N)] for _ in range(N)]
    tmp = []
    for j in range(N):
        for i in range(N):
            if nl[j][i] and not vl[j][i]:
                Q = deque([[i, j]])
                vl[j][i] = True
                while Q:
                    x, y = Q.popleft()
                    tx = x + 1
                    ty = y + 1
                    if tx < N and nl[y][tx] and not vl[y][tx]:
                        vl[y][tx] = True
                        Q.append([tx, y])
                    if ty < N and nl[ty][x] and not vl[ty][x]:
                        vl[ty][x] = True
                        Q.append([x, ty])
                tmp.append([y-j+1, x-i+1])
    cnt = len(tmp)
    ml = deque()
    ml.append(tmp.pop())
    i = 0
    while tmp:
        if tmp[i][0] == ml[-1][1]:
            ml.append(tmp[i])
            tmp[i], tmp[-1] = tmp[-1], tmp[i]
            tmp.pop()
            i = -1
            continue
        elif tmp[i][1] == ml[0][0]:
            ml.appendleft(tmp[i])
            tmp[i], tmp[-1] = tmp[-1], tmp[i]
            tmp.pop()
            i = -1
            continue
        i += 1
    arl = [ml[0][0]]
    for v in ml:
        arl.append(v[1])
    D = [[0xffffffff for _ in range(len(arl))] for _ in range(len(arl))]
    for i in range(len(arl)):
        D[i][i] = 0
    for k in range(1, cnt):
        for l in range(1, cnt - k+1):
            # 가로 k+l 세로l
            for i in range(l, k+l):
                D[l][k + l] = min(D[l][k + l], D[l][i] + D[i+1][k + l] + arl[k+l] * arl[i] * arl[l-1])
            # 0부터 k+l 전까지 & l+1부터

    print('#{} {}'.format(t, D[1][-1]))