import sys
input = sys.stdin.readline
T = int(input())
while T:
    T -= 1
    N = int(input())
    if N == 1:
        input()
        print('YES')
    else:
        nl = list(map(int, input().split()))
        chk = 0
        if nl[0] & 1:
            for i in nl:
                if not (i & 1):
                    print('NO')
                    chk = 1
                    break
        else:
            for i in nl:
                if i & 1:
                    print('NO')
                    chk = 1
                    break
        if not chk:
            print('YES')