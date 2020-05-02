N, M = map(int, input().split())
mod = 998244353
D = [[[0 for _ in range(3)] for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, M+1):
    D[1][i][1] = 1
for j in range(2, N+1):
    for i in range(1, M+1):
        p = j - 1
        q = j + 1
        for k in range(1, i):
            D[j][i][0] += sum(D[p][k])
            D[j][i][0] %= mod
        for k in range(i+1, M+1):
            D[j][i][2] += D[p][k][1] + D[p][k][2]
            D[j][i][2] %= mod
        D[j][i][1] = sum(D[p][i])
        D[j][i][1] %= mod
result = 0
for i in range(1, M+1):
    result += sum(D[N][i])
    result %= mod

print(result)