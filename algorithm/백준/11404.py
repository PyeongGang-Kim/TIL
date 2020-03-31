infd = 10000000001
maxd = 100001

N = int(input())
M = int(input())
nl = [[infd for _ in range(N+1)] for _ in range(N+1)]
ml = [[infd for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    if nl[a][b]:
        nl[a][b] = min(c, nl[a][b])
    else:
        nl[a][b] = c
for i in range(N+1):
    nl[i][i] = 0
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            nl[i][j] = min(nl[i][k] + nl[k][j], nl[i][j])
R = []


for i in range(1, N+1):
    tmp = ''
    for j in range(1, N+1):
        if nl[i][j] == infd:
            tmp = tmp + '0 '
        else:
            tmp = tmp + str(nl[i][j]) + ' '
    R.append(tmp)

print('\n'.join(R))