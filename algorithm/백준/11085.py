import heapq
import sys
input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())
ran = range(p)
ml = [[0 for _ in range(p)] for _ in range(p)]
vl = [False for _ in ran]
while w:
    w -= 1
    s, e, wid = map(int, input().split())
    if ml[s][e]:
        ml[s][e] = min(-wid, ml[s][e])
    else:
        ml[s][e] = -wid
    ml[e][s] = ml[s][e]

Q = [[-50001, c]]
minwidth = -50001
while Q:
    tmp, newp = heapq.heappop(Q)
    minwidth = max(tmp, minwidth)
    if newp == v:
        break
    if not vl[newp]:
        vl[newp] = True
        for i in ran:
            if ml[newp][i] and not vl[i]:
                heapq.heappush(Q, [ml[newp][i], i])
print(-minwidth)