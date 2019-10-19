
T = int(input())
nl = []
mn = 0
for t in range(T):
    tmp =int(input())
    mn = max(mn, tmp)
    nl.append(tmp)
a = [0 for _ in range(mn+1)]
a[0], a[1], a[2] = 1, 1, 3
for i in range(mn-2):
    a[i+3] = a[i]*1+a[i+1]*2+a[i+2]*1

r = []
for i, n in enumerate(nl, 1):
    r.append('#{} {}'.format(i, a[n]))
print('\n'.join(r))
