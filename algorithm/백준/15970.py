# 점의 갯수. 최대 색의 갯수
N = int(input())
cl = [[] for _ in range(N+1)]
nl = [list(map(int, input().split())) for _ in range(N)]
nl.sort(reverse=True)
while nl:
    a, b = nl.pop()
    cl[b].append(a)
# 1부터 길이-1
r = 0
for i in range(1, N+1):
    if cl[i]:
        r += cl[i][1] - cl[i][0] + cl[i][len(cl[i])-1] - cl[i][len(cl[i])-2]
        for j in range(1, len(cl[i]) - 1):
            r += min(cl[i][j]-cl[i][j-1], cl[i][j+1]-cl[i][j])
print(r)

