import sys
input = sys.stdin.readline

def findset(i):
    if cl[i]:
        cl[i] = findset(cl[i])
    else:
        return i
    return cl[i]


N = int(input())
M = int(input())
nl = [[]]
for _ in range(N):
    nl.append([0]+list(map(int, input().split())))
il = list(map(int, input().split()))

cl = [0 for _ in range(N+1)]
for j in range(1, N+1):
    for i in range(1, N+1):
        if nl[j][i]:
            tmp1, tmp2 = findset(i), findset(j)
            if tmp1 != tmp2:
                cl[tmp2] = tmp1
tmp1 = findset(il[0])
chk = False
for i in range(1, N):
    tmp2 = findset(il[i])
    if tmp2 != tmp1:
        chk = True
        break
    tmp1 = tmp2
if chk:
    print('NO')
else:
    print('YES')