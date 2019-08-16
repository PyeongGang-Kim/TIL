import sys
sys.stdin = open("#4835_input.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split(" "))
    ai = list(map(int, input().strip().split(" ")))
    result = 0
    tmp = 0
    for i in range(M):
        tmp += ai[i]
    maxnum, minnum = tmp, tmp

    for n in range(N-M):
        tmp = 0
        for m in range(1, M+1):
            tmp += ai[n+m]
        if tmp > maxnum:
            maxnum = tmp
        if tmp < minnum :
            minnum = tmp

    result = maxnum - minnum
    print('#{} {}'.format(t, result))