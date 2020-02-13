import sys
input = sys.stdin.readline
inf = 0xfffffff
V, E = map(int, input().split())
ran = range(V+1)
nl = [[inf for _ in ran] for _ in ran]
while E:
    E -= 1
    a, b, c = map(int, input().split())
    nl[a][b] = c
dl = [inf] * (V+1)
r = inf
for i in ran:
    nl[i][i] = 0
for k in ran:
    for i in ran:
        for j in ran:
            if i == j and k != i:
                dl[i] = min(dl[i], nl[i][k] + nl[k][j])
                r = min(r, dl[i])
            elif nl[i][k] + nl[k][j] < nl[i][j]:
                nl[i][j] = nl[i][k] + nl[k][j]
if r == inf:
    print(-1)
else:
    print(r)
