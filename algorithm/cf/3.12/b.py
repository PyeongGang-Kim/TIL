import sys
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    N = int(input())

    vl = [0] * (N+1)
    nl = list(map(int, input().split()))
    chk = 0
    for i in range(N):
        if vl[nl[i]]:
            if vl[nl[i]] + 1 <= i:
                chk = 1
                break
        else:
            vl[nl[i]] = i + 1
    print("YES" if chk else "NO")