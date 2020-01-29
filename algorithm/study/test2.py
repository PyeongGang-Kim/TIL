from collections import deque

def mindis():
    Q = deque([[0, 1]])
    while Q:
        dis, idx = Q.popleft()
        for nidx, t in D[idx]:
            if dl[nidx] > dis + t:
                dl[nidx] = dis + t
                Q.append([dl[nidx], nidx])
    return dl[-1]


def subdis(a, b, t):
    Q = deque([[dl[t], t]])
    while Q:
        dis, idx = Q.popleft()
        for nidx, t in D[idx]:
            if ((nidx == b) and (idx == a)) or ((nidx == a) and (idx == b)):
                continue
            if dl[nidx] > dis + t:
                dl[nidx] = dis + t
                Q.append([dl[nidx], nidx])
    return dl[-1]


def check(a, b):
    for ta, t in D[b]:
        if ta == a:
            continue
        if dl[ta] + t == dl[b]:
            return 0
    return b


N, M = map(int, input().split())
D = [[] for i in range(N+1)]
ml = []
while M:
    M -= 1
    a, b, t = map(int, input().split())
    D[a].append([b, t])
    D[b].append([a, t])
    ml.append([a, b])


dl = [0xffffffff] * (N+1)
dl[1] = 0
r1 = mindis()

r2 = 0
for a, b in ml:
    t = 0
    if dl[a] < dl[b]:
        t = check(a, b)
    elif dl[a] > dl[b]:
        t = check(b, a)
    else:
        continue
    if t:
        r2 = max(r2, subdis(a, b, t))
    if r2 == 0xffffffff:
        print(-1)
        break
if r2 != 0xffffffff:
    print(r2 - r1)

