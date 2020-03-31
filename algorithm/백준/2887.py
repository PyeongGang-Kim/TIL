import sys
input = sys.stdin.readline
def findset(i):
    if cl[i] != -1:
        cl[i] = findset(cl[i])
        return cl[i]
    return i


N = int(input())
nl = [list(map(int, input().split())) + [i] for i in range(N)]
ml = []
cl = [-1]*(N+1)
for k in range(3):
    nl.sort(key=lambda x: x[k])
    for i in range(N-1):
        ml.append([abs(nl[i][k] - nl[i+1][k]), nl[i][3], nl[i+1][3]])
ml.sort()
r = 0
for edge in ml:
    t1, t2 = findset(edge[1]), findset(edge[2])
    if t1 != t2:
        cl[t2] = t1
        r += edge[0]
print(r)