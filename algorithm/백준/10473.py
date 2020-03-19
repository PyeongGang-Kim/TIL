import math
import heapq
import sys
input = sys.stdin.readline

def bfs():
    Q = []
    vl = [0xfffffff] * (n+1)
    for i in range(n+1):
        tx, ty = nl[i]
        tmp = math.sqrt((SX-tx)**2 + (SY-ty)**2)/5
        heapq.heappush(Q, [tmp, tx, ty, i])
        vl[i] = tmp
    while Q:
        dis, cx, cy, cidx = heapq.heappop(Q)
        if cidx == n:
            return dis
        if vl[cidx] < dis:
            continue
        for i in range(len(nl)):
            if i == cidx:
                continue
            tx, ty = nl[i]
            tdis = min(math.sqrt((cx - tx)**2 + (cy - ty)**2), abs(math.sqrt((cx - tx)**2 + (cy - ty)**2)-50) + 10)/5 + dis
            if tdis < vl[i]:
                vl[i] = tdis
                heapq.heappush(Q, [tdis, tx, ty, i])


SX, SY = map(float, input().split())
EX, EY = map(float, input().split())
n = int(input())
nl = [list(map(float, input().split())) for _ in range(n)] + [[EX, EY]]
print(bfs())