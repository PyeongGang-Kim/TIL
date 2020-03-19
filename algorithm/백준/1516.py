from collections import deque

def to():
    Q = deque([])
    for i in range(N):
        if not cntl[i][0]:
            Q.append([i, cntl[i][1]])
    while Q:
        idx, dis = Q.popleft()
        for nidx in ml[idx]:
            cntl[nidx][0] -= 1
            cntl[nidx][2] = max(cntl[nidx][2], dis)
            if not cntl[nidx][0]:
                cntl[nidx][1] += cntl[nidx][2]
                Q.append([nidx, cntl[nidx][1]])


N = int(input())
cntl = [[0, 0, 0] for i in range(N)]
ml = [[] for _ in range(N)]
k = 0
while k < N:
    tmp = list(map(int, input().split()))
    cntl[k][1] = tmp[0]
    for i in range(1, len(tmp)-1):
        cntl[k][0] += 1
        ml[tmp[i]-1].append(k)
    k += 1
to()

print('\n'.join(map(str, [i[1] for i in cntl])))
