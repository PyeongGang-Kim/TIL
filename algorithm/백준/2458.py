import sys
input = sys.stdin.readline

inf = 300
n, m = map(int, input().split())
ran = range(n+1)
nl = [[inf for _ in ran] for _ in ran]
i = n
while i:
    nl[i][i] = 0
    i -= 1

while m:
    m -= 1
    u, v = map(int, input().split())
    nl[u][v] = 0

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
r = 0
i = n
while i:
    j = n
    cnt = 0
    while j:
        if not nl[i][j]:
            cnt += 1
        if not nl[j][i]:
            cnt += 1
        j -= 1
    if cnt == n + 1:
        r += 1
    i -= 1

print(r)