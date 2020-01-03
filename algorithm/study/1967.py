import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def dimt(idx):
    global R
    if nl[idx]:
        tmp = 0
        tmp2 = 0
        for i, d in nl[idx]:
            tmp3 = dimt(i)+d
            if tmp3 > tmp:
                tmp2 = tmp
                tmp = tmp3
            elif tmp3 > tmp2:
                tmp2 = tmp3
        R = max(tmp + tmp2, R)
        return tmp
    else:
        return 0


N = int(input())
nl = [[] for _ in range(N+1)]
N -= 1
R = 0
while N:
    p, c, d = map(int, input().split())
    nl[p].append([c, d])
    N -= 1
dimt(1)
print(R)
