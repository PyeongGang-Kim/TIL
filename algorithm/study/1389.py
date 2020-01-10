N, M = map(int, input().split())
nl = [[0xffffffff for _ in range(N+1)] for _ in range(N+1)]
while M:
    M -= 1
    a, b = map(int, input().split())
    nl[a][b] = 1
    nl[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            nl[i][j] = min(nl[i][k] + nl[k][j], nl[i][j])

minnum = 0xfffffff
idx = 0
for j in range(1, N+1):
    tmp = 0
    for i in range(1, N+1):
        tmp += nl[j][i]
    if tmp < minnum:
        minnum = tmp
        idx = j


print(idx)