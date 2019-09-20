N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]
rl = [nl[0][:]]
for i in range(1, N):
    c1 = min(rl[i-1][1], rl[i-1][2]) + nl[i][0]
    c2 = min(rl[i-1][0], rl[i-1][2]) + nl[i][1]
    c3 = min(rl[i-1][1], rl[i-1][0]) + nl[i][2]
    rl.append([c1, c2, c3])
print(min(rl[N-1]))