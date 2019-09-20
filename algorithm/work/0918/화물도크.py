import sys
sys.stdin = open('화물도크.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
    cnt = 0
    tmp = 0
    for n in nl:
        if n[0] >= tmp:
            tmp = n[1]
            cnt += 1
    print('#{} {}'.format(t, cnt))
