import sys
input = sys.stdin.readline
T = int(input())
r = []
while T:
    T -= 1
    N, M = map(int, input().split())
    N = min(M-N, N)
    t1 = 1
    t2 = 1
    while N:
        t1 *= M
        t2 *= N
        M -= 1
        N -= 1
    r.append(str(int(t1/t2)))
print('\n'.join(r))

