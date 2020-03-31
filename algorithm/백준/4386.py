import sys
import heapq
import math
input = sys.stdin.readline


n = int(input())
nl = [list(map(float, input().split())) for _ in range(n)]
ml = [[] for _ in range(n)]
for j in range(n):
    for i in range(n):
        if j != i:
            ml[j].append([(nl[i][0] - nl[j][0])**2 + (nl[i][1] - nl[j][1])**2, j, i])
s = 0
Q = []
for item in ml[0]:
    heapq.heappush(Q, item)
vl = [0] * n
vl[0] = 1
cnt = n-1
while Q:
    dis, idx1, idx2 = heapq.heappop(Q)
    if not vl[idx2]:
        s += math.sqrt(dis)
        for item in ml[idx2]:
            heapq.heappush(Q, item)
        vl[idx2] = 1
        cnt -= 1
    if not cnt:
        break

print(s)