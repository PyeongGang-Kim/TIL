import sys
sys.stdin = open('두더지굴.txt')


def dfs(i, j, d = 1):
    nl[j][i] = 0
    for k in range(4):
        tmpx, tmpy = i + dl[k][0], j + dl[k][1]
        if 0 <= tmpx < N and 0 <= tmpy < N:
            if nl[tmpy][tmpx]:
                d = dfs(tmpx, tmpy, d+1)
    return d

N = 7
nl = [list(map(int, input().split())) for _ in range(N)]
dl = [[0,1],[0,-1],[1,0],[-1,0]]
cnt = 0
result = []
for j in range(N):
    for i in range(N):
        if nl[j][i]:
            result.append(dfs(i, j))
            cnt+=1
result.sort(reverse=True)
print(cnt, result)