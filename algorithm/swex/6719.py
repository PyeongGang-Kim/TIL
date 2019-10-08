T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    nl = sorted(list(map(int, input().split())), reverse=True)
    r = 0
    for i in range(K-1, -1, -1):
        r = (r + nl[i])/2
    print('#{} {:6f}'.format(t, r))
