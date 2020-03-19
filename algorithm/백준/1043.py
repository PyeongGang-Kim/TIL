import sys
input = sys.stdin.readline
def findset(i):
    if cl2[i][0]:
        cl2[i][0] = findset(cl2[i][0])
        return cl2[i][0]
    else:
        return i

N, M = map(int, input().split())
nl = list(map(int, input().split()))
tl = [0] * (N+1)
for i in range(1, len(nl)):
    tl[nl[i]] = 1
tmp = set()
cl = [0] * (N+1)
cl2 = [[0, 1] for _ in range(M+1)]
while M:
    pl = list(map(int, input().split()))
    for j in range(1, len(pl)):
        i = pl[j]
        if cl[i]:
            t1, t2 = findset(cl[i]), findset(M)
            if t1 != t2:
                if t1 > t2:
                    t1, t2 = t2, t1
                cl2[t2][1] += cl2[t1][1]
                cl2[t1][0] = t2
        cl[i] = M
        if tl[i]:
            tmp.add(M)
    M -= 1
tmp2 = set()
for i in tmp:
    tmp2.add(findset(i))

while tmp2:
    cl2[tmp2.pop()][0] = 1
cnt = 0
for i in range(1, len(cl2)):
    if not cl2[i][0]:
        cnt += cl2[i][1]
print(cnt)
