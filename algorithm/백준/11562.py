import sys
input = sys.stdin.readline

inf = 300
n, m = map(int, input().split())
ran = range(n+1)
nl = [[inf for _ in ran] for _ in ran]
i = 1
while i <= n:
    nl[i][i] = 0
    i += 1

while m:
    m -= 1
    u, v, b = map(int, input().split())
    if b:
        nl[u][v] = 0
        nl[v][u] = 0
    else:
        nl[u][v] = 0
        nl[v][u] = 1

k = 1
while k <= n:
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            if nl[i][j] > nl[i][k] + nl[k][j]:
                nl[i][j] = nl[i][k] + nl[k][j]
            j += 1
        i += 1
    k += 1
r = []
k = int(input())
while k:
    k -= 1
    s, e = map(int, input().split())
    r.append(str(nl[s][e]))
print('\n'.join(r))