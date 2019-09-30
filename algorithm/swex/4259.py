T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = input().split()
    r = 0
    for n in nl:
        r += int(n[:-1])**int(n[-1])
    print('#{} {}'.format(t, r))