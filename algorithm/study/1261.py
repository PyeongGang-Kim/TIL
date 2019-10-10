import heapq, sys
'''
우선순위 큐(heapq)를 사용한 다익스트라
갈 곳이 1인 경우 cnt + 1 해주고
아닌 경우에는 cnt 그대로 유지한 채로 큐에 넣어준다.
Q = [[cnt, x, y], ... ] 형태

비짓 리스트 초기값은 최대치(N*M)

'''

N, M = map(int, sys.stdin.readline().split())
nl = [sys.stdin.readline() for _ in range(M)]
r = N*M
vl = [[r for _ in range(N)] for _ in range(M)]
vl[0][0] = 0
Q = [[0, 0, 0]]
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
heapq.heapify(Q)
while Q:
    cnt, x, y = heapq.heappop(Q)
    for dx, dy in d:
        tx, ty = x + dx, y + dy
        if 0 <= tx < N and 0 <= ty < M:
            if nl[ty][tx] == '1':
                if vl[ty][tx] > cnt + 1:
                    vl[ty][tx] = cnt + 1
                    heapq.heappush(Q, [cnt+1, tx, ty])
            else:
                if vl[ty][tx] > cnt:
                    vl[ty][tx] = cnt
                    heapq.heappush(Q, [cnt, tx, ty])
print(vl[-1][-1])