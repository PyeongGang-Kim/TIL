from collections import deque


N, M = map(int, input().split())
ml = [[] for _ in range(N+1)]
i = 0
while i < M:
    i += 1
    a, b = map(int, input().split())
    ml[b].append(a)

maxlen = 0
result = []
vl = [False for _ in range(N+1)]
tmp = []
for i in range(1, N+1):
    Q = deque([i])
    while tmp:
        vl[tmp.pop()] = False
    vl[i] = True
    tmp.append(i)
    cnt = 1
    while Q:
        idx = Q.popleft()
        for newidx in ml[idx]:
            if not vl[newidx]:
                vl[newidx] = True
                tmp.append(newidx)
                Q.append(newidx)
                cnt += 1

    if maxlen < cnt:
        result = [i]
        maxlen = cnt
    elif maxlen == cnt:
        result.append(i)

print(' '.join(map(str, result)))