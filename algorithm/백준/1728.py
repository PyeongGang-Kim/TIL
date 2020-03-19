import sys
input = sys.stdin.readline

def chk(p, v):
    for j in range(2, N+1):
        p += v
        chk = 1
        for i in range(N):
            if nl[j][i] == p:
                chk = 0
                break
        if chk:
            return False
    return True

N = int(input())
nl = [list(map(int, input().split())) for _ in range(N+1)]
nl[0].sort()
r = []
for j in range(N):
    for i in range(N):
        v = nl[1][i] - nl[0][j]
        if chk(nl[1][i], v):
            r.append('{} {}'.format(nl[0][j], v))
            break

print('\n'.join(r))