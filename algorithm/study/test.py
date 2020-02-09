import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nl = []
while M:
    M -= 1
    nl.append(list(map(int, input().split())))
nl.sort(key=lambda x: x[2])
vl = [0] * (N+1)
r = [str(N-1)]
for a, b, d in nl:
    if vl[a] and vl[b]:
        continue
    vl[a] = 1
    vl[b] = 1
    r.append(str('{} {}'.format(a, b)))
print('\n'.join(r))