import math, sys, heapq
input = sys.stdin.readline


T = int(input())
while T:
    T -= 1
    r = 0
    W = int(input())
    N = int(input())
    if not N:
        print(W/2)
        continue
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [0] * (N+2)
    vl[-1] = 1
    Q = []
    for i in range(N):
        heapq.heappush(Q, [nl[i][0]-nl[i][2], i])
    while Q:
        dis, idx = heapq.heappop(Q)
        r = max(r, dis)
        if idx == N:
            break

        if not vl[idx]:
            vl[idx] = 1
            for i in range(N):
                if not vl[i] and idx != i:
                    heapq.heappush(Q, [math.sqrt((nl[i][0] - nl[idx][0]) ** 2 + (nl[i][1] - nl[idx][1]) ** 2) - (nl[i][2] + nl[idx][2]), i])
            heapq.heappush(Q, [W - (nl[idx][0]+nl[idx][2]), N])
    print(r/2 if r > 0 else 0)