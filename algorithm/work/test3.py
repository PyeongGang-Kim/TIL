from collections import deque

def bfs(p, cnt = 0):
    Q = deque([[p, cnt]])
    tmp.add(p)

    while Q:
        p, cnt = Q.popleft()
        if p == b:
            return cnt
        if p-1 not in tmp and p >= 0:
            tmp.add(p-1)
            Q.append([p-1, cnt+1])
        if p+1 not in tmp and p < b:
            tmp.add(p+1)
            Q.append([p+1, cnt+1])
        if p*2 not in tmp and p < b:
            tmp.add(p*2)
            Q.append([p*2, cnt+1])


a, b = map(int, input().split())
tmp = set()
print(bfs(a))