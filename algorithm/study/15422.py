import sys
import heapq
# input = sys.stdin.readline
sys.stdin = open('asdf.txt'
)
def bfs(s, t):
    vl = [[0xffffffffff, 0xffffffffff] for _ in range(n)]
    vl[s][0] = 0
    vl[s][1] = 0
    Q = [[0, s, 1]]

    while Q:
        dis, pos, chk = heapq.heappop(Q)
        if pos == t:
            return dis
        if dis > vl[pos][chk]:
            continue
        for npos, tdis in nl1[pos]:
            ndis = dis + tdis
            if ndis < vl[npos][chk]:
                vl[npos][chk] = ndis
                heapq.heappush(Q, [ndis, npos, chk])
        if chk:
            for npos in nl2[pos]:
                if dis < vl[npos][0]:
                    vl[npos][0] = dis
                    heapq.heappush(Q, [dis, npos, 0])


n, m, f, s, t = map(int, input().split())
nl1 = {i: [] for i in range(n)}
nl2 = [set() for _ in range(n)]
while m:
    m -= 1
    a, b, c = map(int, input().split())
    nl1[a].append([b, c])
    nl1[b].append([a, c])
while f:
    f -= 1
    a, b = map(int, input().split())
    nl2[a].add(b)

print(bfs(s, t))