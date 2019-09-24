import sys
sys.stdin = open('연산.txt')


from collections import deque


def bfs(a):
    Q = deque()
    Q.append([a, 0])
    tmp.add(a)
    while Q:
        p, cnt = Q.popleft()
        if p == b:
            return cnt
        for fx in D:
            x = fx(p)
            if 0 <= x < 2*b and x not in tmp:
                Q.append([x, cnt+1])
                tmp.add(x)


D = [lambda x: x+1, lambda x: x-1, lambda x: x*2, lambda x: x-10]
T = int(input())
for t in range(1, T+1):
    tmp = set()
    a, b = map(int, input().split())

    print('#{} {}'.format(t, bfs(a)))