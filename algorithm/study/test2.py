from collections import deque

def dfs(i, dep = 1):
    if nl[i][1]:
        nl[i][0] = dep
        return nl[i][1]
    tmp = 1
    for idx in range(1, N+1):
        if ml[i][idx]:
            tmp += dfs(idx, dep + 1)
    nl[i][1] = tmp
    return tmp

N, M = map(int, input().split())

ml = [[False for _ in range(N+1)] for _ in range(N+1)]
ml2 = [[False for _ in range(N+1)] for _ in range(N+1)]
while M:
    M -= 1
    a, b = map(int, input().split())
    ml[a][b] = True
    ml2[b][a] = True

nl = [[0, 0] for _ in range(N+1)]
#vl = [False for _ in range(N+1)]
imp = set()
tmp = (N+1)//2
for i in range(1, N+1):
    if not nl[i][0]:
        dfs(i)
for i in range(1, N+1):
    if nl[i][0] > tmp:
        imp.add(i)
    if nl[i][1] > tmp:
        imp.add(i)

print(len(imp))
