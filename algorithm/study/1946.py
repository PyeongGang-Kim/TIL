import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    nl.sort()
    r = 1
    tmp = nl[0][1]
    for i in range(1, N):
        if tmp > nl[i][1]:
            tmp = nl[i][1]
            r += 1
    print(r)