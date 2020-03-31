from collections import deque
'''
0이 담긴 위치들 리스트
3개 선정하는 for문
각각의 경우에 대해서 초기화 후 bfs
0갯수 센다
bfs 체크 될 때마다 tmp변수 +1
결과값에 저장
'''


def bfs(i, j):
    cnt = 0
    Q = deque([(i, j)])
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < M and 0 <= ty < N:
                if nl2[ty][tx] == '0':
                    nl2[ty][tx] = '2'
                    cnt += 1
                    Q.append((tx, ty))
    return cnt


d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
N, M = map(int, input().split())
nl = [input().split() for _ in range(N)]
zl = []
vl = []
r = 0
for j in range(N):
    for i in range(M):
        if nl[j][i] == '0':
            zl.append((i, j))
        if nl[j][i] == '2':
            vl.append((i, j))

for b1 in range(0, len(zl)-2):
    nl[zl[b1][1]][zl[b1][0]] = '1'
    for b2 in range(b1+1, len(zl)-1):
        nl[zl[b2][1]][zl[b2][0]] = '1'
        for b3 in range(b2+1, len(zl)):
            nl[zl[b3][1]][zl[b3][0]] = '1'
            nl2 = []
            for n in range(N):
                nl2.append(nl[n][:])
            tmp = 0
            for vx, vy in vl:
                tmp += bfs(vx, vy)
            if len(zl)-tmp - 3 > r:
                r = len(zl) - tmp - 3
            nl[zl[b3][1]][zl[b3][0]] = '0'
        nl[zl[b2][1]][zl[b2][0]] = '0'
    nl[zl[b1][1]][zl[b1][0]] = '0'
print(r)