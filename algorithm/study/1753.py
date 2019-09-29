'''
다익스트라 알고리즘 사용.
단순한 bfs 시 시간초과 문제가 있다.
=> 최소힙 사용으로 가장 짧은 경로들을 모두 갱신하여 불필요한 연산을 줄인다.
+ input() 대신에 sys.stdin.readline()을 사용한다.


'''

import sys
import heapq
def bfs(i):
    Q = [[0, i]]
    heapq.heapify(Q)
    vl[i] = 0
    while Q:
        d, idx = heapq.heappop(Q)
        if vl[idx] >= d:
            for v, w in ml[idx]:
                if vl[idx] + w < vl[v]:
                    vl[v] = vl[idx] + w
                    heapq.heappush(Q, [vl[v], v])


V, E = map(int, input().split())
i = int(input())
ml = {n: [] for n in range(1, V+1)}
for k in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    ml[u].append([v, w])


vl = [3000001 for _ in range(V+1)]
bfs(i)
vl[i] = 0
r = []
for i in range(1, V+1):
    if vl[i] == 3000001:
        r.append('INF')
    else:
        r.append(str(vl[i]))
print('\n'.join(r))