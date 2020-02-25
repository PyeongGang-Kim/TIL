import sys
input = sys.stdin.readline


def findset(i):
    if not cl[i]:
        return i
    cl[i] = findset(cl[i])
    return cl[i]

N, M = map(int, input().split())
ml = []
while M:
    M -= 1
    a, b, c = map(int, input().split())
    ml.append([c, a, b])
ml.sort()
cl = [0] * (N+1)
s = 0
cnt = N - 2
for c, a, b in ml:
    t1, t2 = findset(a), findset(b)
    if t1 != t2:
        cl[t2] = t1
        s += c
        cnt -= 1
        if not cnt:
            break
print(s)