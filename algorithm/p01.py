from collections import deque

d = [[0, 1], [0, -1], [-1, 0], [1, 0]]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(N)]
    sumall = 0
    cntall = 0
    for j in range(N):
        for i in range(M):
            sumall += nl[j][i]
            cntall += 1
    kl = []
    for _ in range(K):
        kl.append(list(map(int, input().split())))
    for k in kl:
        disk, rotate, num_rotate = k
        if not rotate:
            num_rotate = (-num_rotate) % 4

        for idx in range(disk-1, N, disk):
            for _ in range(num_rotate):
                for m in range(M-1):
                    nl[idx][m], nl[idx][m+1] = nl[idx][m+1], nl[idx][m]

        vl = [[False for _ in range(M)] for _ in range(N)]
        samechk = False
        for j in range(N):
            for i in range(M):
                if nl[j][i] and not vl[j][i]:
                    vl[j][i] = True
                    cur = nl[j][i]
                    Q = deque([[i, j]])
                    chk = False
                    while Q:
                        x, y = Q.popleft()
                        for dx, dy in d:
                            tx, ty = (x + dx) % M, y + dy
                            if 0 <= ty < N and not vl[ty][tx] and nl[ty][tx] == cur:
                                chk = True
                                samechk = True
                                sumall -= nl[ty][tx]
                                cntall -= 1
                                nl[ty][tx] = 0
                                vl[ty][tx] = True
                                Q.append([tx, ty])
                    if chk:
                        sumall -= cur
                        cntall -= 1
                        nl[j][i] = 0
        if not cntall:
            break
        if not samechk:
            tmp = sumall // cntall
            for j in range(N):
                for i in range(M):
                    if nl[j][i] < tmp:
                        nl[j][i] += 1
                    elif nl[j][i] > tmp:
                        nl[j][i] -= 1

    print(sumall)


