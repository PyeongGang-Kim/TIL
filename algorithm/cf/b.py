n = int(input())
nl = list(map(int, input().split()))
D = [[0, 0] for _ in range(n)]
D[0][0] = nl[0]
D[0][1] = min(nl[0], nl[1])
for i in range(1, n):
    if nl[i] > nl[i-1]:
        D[i][0] = D[i-1][0] + nl[i]
        D[i][1] = D[i-1][1] + nl[i-1]
    else:
        D[i][0] = D[i-1][1] + nl[i]
        D[i][1] = D[i-1][0] + nl[i]
print()