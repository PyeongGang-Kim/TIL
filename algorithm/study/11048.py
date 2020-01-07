import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
D = [[0 for _ in range(M)] for _ in range(N)]
D[0][0] = nl[0][0]
for j in range(1, N):
    D[j][0] = D[j-1][0] + nl[j][0]
for i in range(1, M):
    D[0][i] = D[0][i-1] + nl[0][i]
for j in range(1, N):
    for i in range(1, M):
        D[j][i] = max(D[j-1][i], D[j][i-1], D[j-1][i-1]) + nl[j][i]
print(D[-1][-1])

