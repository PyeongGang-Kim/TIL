from collections import deque
def bfs(i, j):
    Q = deque([[i, j, 0]])
    vl = [[0 for _ in range(M)] for _ in range(N)]
    vl[j][i] = 1
    while Q:
        x, y, d = Q.popleft()
        if d == D:
            return -1, -1
        if (x, y) in tes:
            return x, y
        for dx, dy in Di:
            tx, ty = x + dx, y + dy
            if 0 <= tx < M and 0 <= ty < N and not vl[ty][tx]:
                vl[ty][tx] = 1
                Q.append([tx, ty, d+1])
    return -1, -1



Di = [[-1, 0], [0, -1], [1, 0]]
N, M, D = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
es = set()
for j in range(N):
    for i in range(M):
        if nl[j][i]:
            es.add((i, j))
r = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            tes = set()
            for data in es:
                tes.add(data)
            cnt = 0
            while tes:
                t1, t2 = bfs(i, N-1)
                t3, t4 = bfs(j, N-1)
                t5, t6 = bfs(k, N-1)
                if t1 != -1:
                    if (t1, t2) in tes:
                        tes.remove((t1, t2))
                        cnt += 1
                if t3 != -1:
                    if (t3, t4) in tes:
                        tes.remove((t3, t4))
                        cnt += 1
                if t5 != -1:
                    if (t5, t6) in tes:
                        tes.remove((t5, t6))
                        cnt += 1
                tes2 = set()
                for x, y in tes:
                    if y != N:
                        tes2.add((x, y+1))
                tes = tes2
            r = max(cnt, r)
print(r)