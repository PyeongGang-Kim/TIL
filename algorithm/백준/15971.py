import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(i, maxd=0, sumd=0):
    global result
    if i == r2:
        result = min(result, sumd - maxd)
        return
    for idx, dis in nl[i]:
        if not vl[idx]:
            vl[idx] = True
            tempmaxd = max(maxd, dis)
            tempsumd = sumd + dis
            if result <= tempsumd - tempmaxd:
                return
            dfs(idx, tempmaxd, tempsumd)
            vl[idx] = False


N, r1, r2 = map(int, input().split())
nl = [[] for _ in range(N+1)]
i = 1
while i < N:
    a, b, c = map(int, input().split())
    nl[a].append([b, c])
    nl[b].append([a, c])
    i += 1
vl = [False for _ in range(N+1)]
vl[r1] = True
result = 0xfffffff
dfs(r1)


print(result)