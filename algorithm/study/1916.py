import heapq
import sys
'''
힙을 이용한 다익스트라
힙에서 빼온 데이터의 거리가 vl에 저장된 거리보다 클 경우 넘겨준다.
'''
def bfs():
    Q = [[0, S]]
    heapq.heapify(Q)
    vl[S] = 0
    while Q:
        dis, idx = heapq.heappop(Q)
        if dis > vl[idx]:
            continue
        for dis, v in ml[idx]:
            tmp = vl[idx]+dis
            if vl[v] > tmp:
                vl[v] = tmp
                heapq.heappush(Q, [vl[v], v])

N = int(input())
M = int(input())
ml = {i: [] for i in range(1, N+1)}
vl = [0xfffffff for i in range(N+1)]
for i in range(M):
    t1, t2, v = map(int, sys.stdin.readline().split())
    ml[t1].append([v, t2])
S, G = map(int, input().split())
bfs()
print(vl[G])