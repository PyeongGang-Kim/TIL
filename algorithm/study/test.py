from collections import deque
N, M = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
pl = []
vl = []
D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
cntmin = 999999
cnta = 0
for j in range(N):
    for i in range(M):
        if nl[j][i]:
            vl.append((i, j))
        else:
            pl.append((i, j))
            cnta += 1

for k in range(len(pl)-2):
    for l in range(k+1, len(pl)-1):
        for m in range(l+1, len(pl)):
            print(k, l, m)


            nnl = []
            for n in range(N):
                nnl.append(nl[n][:])

            nnl[pl[k][1]][pl[k][0]] = 1
            nnl[pl[l][1]][pl[l][0]] = 1
            nnl[pl[m][1]][pl[m][0]] = 1
            Q = deque()
            # cnt = 0
            # for v in vl:
            #     Q.append(v)
            # while Q:
            #     x, y = Q.popleft()
            #     for dx, dy in D:
            #         tx, ty = x + dx, y + dy
            #         if 0 <= tx < M and 0 <= ty < N and not nnl[ty][tx]:
            #             nnl[ty][tx] = 0
            #             cnt += 1
            #             Q.append((tx, ty))
            # cntmin = min(cntmin, cnt)

print(cnta - cntmin)

