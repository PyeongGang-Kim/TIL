from collections import deque

def bfs():
    Q.append(1)
    while Q:
        currentPosition = Q.popleft()
        for nextPosition in nl[currentPosition]:
            if not vl[nextPosition]:
                vl[nextPosition] = True
                Q.append(nextPosition)
                rl[nextPosition] = currentPosition

N = int(input())
nl = [[] for _ in range(N+1)]
vl = [False for _ in range(N+1)]
rl = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    nl[a].append(b)
    nl[b].append(a)

Q = deque()
bfs()
r = []
for i in range(2, N+1):
    r.append(str(rl[i]))
print('\n'.join(r))