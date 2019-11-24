import sys
input = sys.stdin.readline

import heapq
N = int(input())
nl = [int(input()) for _ in range(N)]
Q = []
r = []
for n in nl:
    if n:
        heapq.heappush(Q, n)
    else:
        if Q:
            r.append(str(heapq.heappop(Q)))
        else:
            r.append('0')
print('\n'.join(r))