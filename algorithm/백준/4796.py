L, P, V = map(int, input().split())
r = []
i = 0
while L or P or V:
    i += 1
    tmp1, tmp2 = divmod(V, P)
    tmp = tmp1*L + min(tmp2, L)
    r.append('Case {}: {}'.format(i, tmp))
    L, P, V = map(int, input().split())
print('\n'.join(r))