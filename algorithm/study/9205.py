from collections import deque
'''
bfs문제
'''
r = []
T = int(input())
for t in range(T):
    N = int(input())
    Q = deque()
    Q.append(tuple(map(int, input().split())))
    vl = {}
    for _ in range(N):
        vl[tuple(map(int,input().split()))] = False

    G = tuple(map(int, input().split()))
    r.append('sad')
    while Q:
        P = Q.popleft()
        tmp = abs(P[0]-G[0]) + abs(P[1]-G[1])
        if tmp <= 1000:
            r[t] = 'happy'
            break
        for key, value in vl.items():
            if not value:
                tmp = abs(P[0]-key[0]) + abs(P[1]-key[1])
                if tmp <= 1000:
                    Q.append(key)
                    vl[key] = True
print('\n'.join(r))