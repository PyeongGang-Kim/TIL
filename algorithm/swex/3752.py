r = []
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    tmp = {0}
    for i in range(N):
        tmp1 = set()
        for j in tmp:
            tmp1.add(j+nl[i])
        tmp = tmp.union(tmp1)
    r.append('#{} {}'.format(t, len(tmp)))
print('\n'.join(r))