def solve(dep=0, cw=0, cv=0):
    global R
    if cw > W:
        return
    if dep == n:
        R = max(R, cv)
        return

    solve(dep+1, cw+weight[dep], cv+value[dep])
    solve(dep+1, cw, cv)

W = 10
n = 4
weight = [5, 4, 6, 3]
value = [10, 40, 30, 50]
A = [0]*n
ans = 0
R = 0

solve()
print(R)

D = [[0 for _ in range(W+1)] for _ in range(n+1)]
for j in range(1, n+1):
    for i in range(1, W+1):
        if i > weight[j-1]:
            D[j][i] = max(D[j-1][i], D[j-1][i-weight[j-1]] + value[j-1])
        else:
            D[j][i] = D[j-1][i]
print(D[-1][-1])