from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global num
    Q = deque([[i, j]])
    vl[j][i] = True
    while Q:
        x, y = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < C and 0 <= ty < R and not vl[ty][tx]:
                if nl[ty][tx] != 'X':
                    vl[ty][tx] = True
                    Q.append([tx, ty])
                    ml[ty][tx] = [i, j]
                else:
                    tmp.add((tx, ty))
    num += 1


def findset(i, j):
    if ml[j][i] != (i, j):
        ml[j][i] = findset(*ml[j][i])
    return ml[j][i]


D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
R, C = map(int, input().split())
tmp = set()
nl = [list(input().strip()) for _ in range(R)]
ml = [[(i, j) for i in range(C)] for j in range(R)]
vl = [[False for _ in range(C)] for _ in range(R)]
L = []
num = 1
for j in range(R):
    for i in range(C):
        if nl[j][i] != 'X':
            if nl[j][i] == 'L':
                L.append([i, j])
            if not vl[j][i]:
                bfs()

day = 0
while findset(*L[0]) != findset(*L[1]):
    day += 1
    Q = list(tmp)
    tmp = set()
    tmp2 = set()
    for x, y in Q:
        nl[y][x] = '.'
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < C and 0 <= ty < R:
                if nl[ty][tx] != 'X':
                    tmp2.add(findset(tx, ty))
                else:
                    tmp.add((tx, ty))
        if len(tmp2) == 1:
            ml[y][x] = tmp2.pop()
        else:
            ml[y][x] = tmp2.pop()
            while tmp2:
                tmp3 = findset(*tmp2.pop())
                ml[tmp3[1]][tmp3[0]] = ml[y][x]


print(day)