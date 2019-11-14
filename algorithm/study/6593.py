from collections import deque
import sys
input = sys.stdin.readline
def finds():
    global S
    for j in range(R):
        for i in range(C):
            if nl[l][j][i] == 'S':
                S = [l, i, j]
                return True
    return False


drs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

Q = deque()
L, R, C = map(int, input().strip().split())
while L and R and C:
    vl = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    nl = []
    l = 0

    chk = False
    while l < L:
        tl = [input().strip() for _ in range(R)]
        input()
        nl.append(tl)
        if not chk:
            finds()
        l += 1
    vl[S[0]][S[2]][S[1]] = True
    Q.append([*S, 0])
    chk = False
    while Q:
        l, x, y, tim = Q.popleft()
        if nl[l][y][x] == 'E':
            chk = True
            Q.clear()
            break
        for dl, dx, dy in drs:
            tl, tx, ty = l + dl, x + dx, y + dy
            if 0 <= tl < L and 0 <= tx < C and 0 <= ty < R and not vl[tl][ty][tx] and (nl[tl][ty][tx] == '.' or nl[tl][ty][tx] == 'E'):
                vl[tl][ty][tx] = True

                Q.append([tl, tx, ty, tim+1])
    if chk:
        print('Escaped in {} minute(s).'.format(tim))
    else:
        print('Trapped!')
    L, R, C = map(int, input().strip().split())

