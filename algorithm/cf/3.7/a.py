import sys

def perm(idx = 0, s = 0):
    if s > i:
        return False
    if s == i:
        return True
    if idx >= N:
        return False
    if perm(idx+1, s):
        return True
    arr.append(idx+1)
    if perm(idx+1, s+nl[idx]):
        return True
    arr.pop()

input = sys.stdin.readline
T = int(input())
while T:
    T -= 1
    N = int(input())
    a = 1
    nl = list(map(int, input().split()))
    for b in nl:
        a |= a << b
    arr = []
    for i in range(2, len(bin(a))-2, 2):
        if a & (1<<i):
            perm()
            break
    if arr:
        print(len(arr))
        print(' '.join(map(str, arr)))
    else:
        print(-1)
