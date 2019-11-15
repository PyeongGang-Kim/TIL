'''
가장 높은곳과 가장 낮은곳을 제한하면서 bfs를 돌려 본다.
모두 방문 될 경우 구간을 더 줄일수 있음
모두 방문 안될 경우 구간을 더 늘려야함
이분탐색
'''
from collections import deque


def bs(s, e):
    if s+1 == e:
        global Max
        if bfs(Min, s):
            Max = s
        else:
            Max = e
        return
    m = (s+e)//2
    if bfs(Min, m):
        bs(s, m)
    else:
        bs(m, e)


def bs2(s, e):
    if s+1 == e:
        global Min
        if bfs(e, Max):
            Min = e
        else:
            Min = s
        return
    m = (s+e)//2
    if bfs(m, Max):
        bs2(m, e)
    else:
        bs2(s, m)


def bfs(s, e):
    if not s <= ml[P[1]][P[0]] <= e:
        return False
    vl = [[False for _ in range(N)] for _ in range(N)]
    vl[P[1]][P[0]] = True
    Q.append(P)
    cnt2 = 0
    while Q:
        x, y = Q.popleft()
        if cnt2 == cnt:
            Q.clear()
            return True
        for dx, dy in dr:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx] and s <= ml[ty][tx] <= e:
                vl[ty][tx] = True
                if nl[ty][tx] == 'K':
                    cnt2 += 1
                Q.append([tx, ty])
    return False

Q = deque()
dr = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
N = int(input())
nl = [input() for _ in range(N)]
ml = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for j in range(N):
    for i in range(N):
        if nl[j][i] == 'P':
            P = [i, j]
        elif nl[j][i] == 'K':
            cnt += 1
Min = 0
Max = 1000000
bs(Min, Max)
bs2(Min, Max)
r1 = [Max - Min]

Min = 0
Max = 1000000
bs2(Min, Max)
bs(Min, Max)
r1.append(Max-Min)
print(r1)