T = int(input())
for t in range(1, T+1):
    N = int(input())
    K = int(input())
    nl = set(map(int, input().split()))
    if len(nl) > K:
        nl = sorted(list(nl))
        dl = sorted([nl[i+1]-nl[i] for i in range(len(nl)-1)])
        tmp = 0
        for i in range(len(nl)-K):
            tmp += dl[i]
        r = tmp
    else:
        r = 0
    print('#{} {}'.format(t, r))
