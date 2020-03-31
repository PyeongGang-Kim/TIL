import sys
input = sys.stdin.readline
inf = 0xfffffff
V, E = map(int, input().split())
nl = [[inf for _ in range(V+1)] for _ in range(V+1)]
while E:
    E -= 1
    a, b, c = map(int, input().split())
    nl[a][b] = c
dl = [inf] * (V+1)
r = inf
for i in range(1, V+1):
    nl[i][i] = 0
for k in range(V+1):
    for i in range(V+1):
        for j in range(V+1):
            if i == j and k != i:
                dl[i] = min(dl[i], nl[i][k] + nl[k][j])
                r = min(r, dl[i])
            elif nl[i][k] + nl[k][j] < nl[i][j]:
                nl[i][j] = nl[i][k] + nl[k][j]
if r == inf:
    print(-1)
else:
    print(r)
