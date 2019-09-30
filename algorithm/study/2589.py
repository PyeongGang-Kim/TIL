from collections import deque
'''

시행착오
bfs를 한번 해서 가장 먼 곳을 고르고 거기서 가장 먼곳까지의 거리를 측정하면 틀림

팁
모든 좌표 말고 유력후보 좌표(구석(물이랑 닿은 부분이 2군데 이상))을 골라서 bfs 실시하면 경우의 수가 줄어든다.
'''
def bfs(i, j):
    global R
    Q = deque([(i, j, 0)])
    vl[j][i] = 1
    while Q:
        x, y, d = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < M and 0 <= ty < N and not vl[ty][tx] and nl[ty][tx] == 'L':
                vl[ty][tx] = 1
                Q.append((tx, ty, d+1))
    R = max(R, d)


D = [[0, 1], [0, -1], [-1, 0], [1, 0]]
N, M = map(int, input().split())
nl = [input() for _ in range(N)]
R = 0

for j in range(N):
    for i in range(M):
        if nl[j][i] == 'L':
            vl = [[0 for _ in range(M)] for _ in range(N)]
            bfs(i, j)
print(R)