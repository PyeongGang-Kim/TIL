import sys
input = sys.stdin.readline

inf = 0xfffffff
n, k = map(int, input().split())
ml = [[inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    ml[i][i] = 0
while k:
    k -= 1
    a, b = map(int, input().split())
    ml[a][b] = 1
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if ml[i][j] > ml[i][k] + ml[k][j]:
                ml[i][j] = ml[i][k] + ml[k][k]
s = int(input())
r = []
while s:
    s -= 1
    a, b = map(int, input().split())
    if ml[a][b] > ml[b][a]:
        r.append(str('1'))
    elif ml[a][b] < ml[b][a]:
        r.append(str('-1'))
    else:
        r.append(str('0'))
print('\n'.join(r))