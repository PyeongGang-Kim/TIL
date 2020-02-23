import sys
input = sys.stdin.readline
inf = 0xfffffff
N = int(input())
M = int(input())
nl = [[inf for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    nl[i][i] = 0

while M:
    M -= 1
    a, b = map(int, input().split())
    nl[a][b] = 1
    nl[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            nl[i][j] = min(nl[i][k] + nl[k][j], nl[i][j])
r = []
cnt = 0
vl = [0 for _ in range(N+1)]
for j in range(1, N+1):
    if vl[j]:
        continue
    tmp = [j]
    cnt += 1
    vl[j] = 1
    for i in range(j+1, N+1):
        if nl[j][i] != inf:
            vl[i] = 1
            tmp.append(i)

    tmp2 = 0 # 최대 경로 인덱스 저장
    tmp3 = 0xfffffff # 최대 경로 저장
    for k in tmp:
        tmp4 = -1
        for i in range(1, N+1):
            if nl[k][i] != inf:
                if tmp4 < nl[k][i]:
                    tmp4 = nl[k][i]
        if tmp3 > tmp4:
            tmp3 = tmp4
            tmp2 = k
    r.append(tmp2)
print(cnt)
r.sort()
print('\n'.join(map(str, r)))