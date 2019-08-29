import sys
sys.stdin = open('미로의거리.txt')


def bfs():
    Q = []
    x, y = S
    d = 0
    Q.append([x, y, d])
    while Q:
        x, y, d = Q.pop(0)
        for i in range(4):
            tx, ty = x + dr[i][0], y + dr[i][1]
            if 0 <= tx < N and 0 <= ty < N:
                if nl[ty][tx] == 3:
                    return d
                if not nl[ty][tx]:
                    nl[ty][tx] = 1
                    Q.append([tx, ty, d+1])
    return 0

results = []
dr = [[0, -1], [0, 1], [-1, 0], [1, 0]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, list(input()))) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if nl[j][i] == 2:
                S = [i, j]
            elif nl[j][i] == 3:
                G = [i, j]
    results.append('#{} {}'.format(t, bfs()))
print('\n'.join(results))