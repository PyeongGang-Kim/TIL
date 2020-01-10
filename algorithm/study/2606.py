import sys
input = sys.stdin.readline
def unionfind(i):
    if cl[i][0]:
        cl[i][0] = unionfind(cl[i][0])
        return cl[i][0]
    return i


N = int(input())
cl = [[0, 1] for _ in range(N+1)]
M = int(input())
while M:
    M -= 1
    a, b = map(int, input().split())
    t1, t2 = unionfind(a), unionfind(b)
    if t1 != t2:
        if t1 > t2:
            t1, t2 = t2, t1
        cl[t2][0] = t1
        cl[t1][1] += cl[t2][1]
print(cl[1][1]-1)