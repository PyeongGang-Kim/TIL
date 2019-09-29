from collections import deque
def bfs(i):
    Q = deque([i])
    vl[i] = 1
    d = L[i]
    while Q:
        idx = Q.popleft()
        for m in ml[idx]:
            if not vl[m]:
                vl[m] = 1
                if L[m] < d:
                    d = L[m]
                Q.append(m)
    return d


N, M, K = map(int, input().split())
ml = {i: [i-1, i+1] for i in range(1, N+1)}
ml[N][-1] = 1
L = [0] + list(map(int, input().split()))
for m in range(M):
    t1, t2 = map(int, input().split())
    if t1 < t2:
        if t1+1 == t2:
            ml[t1].pop()
            ml[t2].pop(0)
        else:
            ml[t2].pop()
            ml[t1].pop(0)
    elif t2+1 == t1:
        ml[t2].pop()
        ml[t1].pop(0)
    else:
        ml[t1].pop()
        ml[t2].pop(0)
vl = [0 for i in range(N+1)]

for i in range(1, N+1):
    if not vl[i]:
        K -= bfs(i)
        if K < 0:
            break

if K < 0:
    print('NO')
else:
    print('YES')