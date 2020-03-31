import sys
'''
dfs로 좌, 우, 아래만 향하면 ㅗㅜㅓㅏ 모양 빼고 모든 조합이 나올 수 있다.
모든 좌표에서 좌 우 아래에 대해서 dfs 탐색 후 ㅗㅜㅓㅏ 모양에 대해서 탐색하면 된다.

'''
def dfs(i, j, s, dep=0):
    if dep == 3:
        global r
        r = max(r, s)
        return
    for dx, dy in d:
        tx, ty = i + dx, j + dy
        if 0 <= tx < M and 0 <= ty < N and not vl[ty][tx]:
            vl[ty][tx] = True
            dfs(tx, ty, s+nl[ty][tx], dep+1)
            vl[ty][tx] = False


input = lambda: sys.stdin.readline()
N, M = map(int, input().split())
ran = range(N)
ram = range(M)
nl = [list(map(int, input().split())) for _ in ran]
vl = [[False for _ in ram] for _ in ran]
d = [[-1, 0], [0, 1], [1, 0]]
r = 0
for j in ran:
    for i in ram:
        vl[j][i] = True
        dfs(i, j, nl[j][i])
        vl[j][i] = False

for j in range(1, N-1):
    for i in range(M-1):
        tmp = nl[j][i] + nl[j][i+1]
        tmp2 = max(nl[j-1][i] + nl[j+1][i], nl[j-1][i+1] + nl[j+1][i+1])
        r = max(r, tmp+tmp2)

for j in range(N-1):
    for i in range(1, M-1):
        tmp = nl[j][i] + nl[j+1][i]
        tmp2 = max(nl[j][i-1] + nl[j][i+1], nl[j+1][i-1] + nl[j+1][i+1])
        r = max(r, tmp+tmp2)

print(r)