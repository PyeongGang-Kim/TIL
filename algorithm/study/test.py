import heapq
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ml = [list(map(int, input().split())) for _ in range(N)]
    r = 0
    for i in range(N):
        vl = [0xffffffff for _ in range(N)]
        vl[i] = 0
        Q = [[0, i]]
        while Q:
            print(i)
            d, idx = heapq.heappop(Q)
            if vl[idx] < d:
                continue
            for j in range(N):
                if ml[idx][j] and ml[idx][j] + vl[idx] < vl[j]:
                    heapq.heappush(Q, [d+ml[idx][j], j])
                    vl[j] = d+ml[idx][j]
        r = max(r, max(vl))
    print(r)