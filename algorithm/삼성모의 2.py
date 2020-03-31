from collections import deque

def select(g, r, selected=[], dep=0):
    if not g and not r:
        bfs(selected)
        return
    if dep == len(land):
        return
    if g:
        selected.append([0, land[dep]])
        select(g-1, r, selected, dep+1)
        selected.pop()
    if r:
        selected.append([1, land[dep]])
        select(g, r-1, selected, dep+1)
        selected.pop()
    select(g, r, selected, dep+1)


def bfs(selected):
    global r
    Q = deque(selected)
    cnt = 0
    vl = [[0 for _ in range(M)] for _ in range(N)]
    for c, pos in selected:
        vl[pos[1]][pos[0]] = 1
    while Q:
        tmp = len(Q)
        tmppos = {}
        while Q:
            c, pos = Q.popleft()
            for dx, dy in D:
                x, y = pos[0] + dx, pos[1] + dy
                if 0 <= x < M and 0 <= y < N and nl[y][x] and not vl[y][x]:
                    if tmppos.get((x, y)) is not None:
                        if c ^ tmppos.get((x, y)):
                            tmppos[(x, y)] = 2
                    else:
                        tmppos[(x, y)] = c
        for pos, c in tmppos.items():
            if c == 2:
                cnt += 1
            else:
                Q.append([c, pos])
            vl[pos[1]][pos[0]] = 1
    r = max(r, cnt)


D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
N, M, G, R = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
land = []
r = 0
for j in range(N):
    for i in range(M):
        if nl[j][i] == 2:
            land.append([i, j])
select(G, R)
print(r)

