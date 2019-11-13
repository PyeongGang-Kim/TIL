from collections import deque

N, K = map(int, input().split())
Q = deque()
Q.append([N, 0])
vl = set()
vl.add(N)
while Q:
    i, tim = Q.popleft()
    if i == K:
        break

    elif i < 1:
        if i+1 not in vl:
            vl.add(i+1)
            Q.append([i+1, tim+1])

    elif i > K:
        if i-1 not in vl:
            vl.add(i-1)
            Q.append([i-1, tim+1])

    else:
        if i+1 not in vl:
            vl.add(i+1)
            Q.append([i+1, tim+1])

        if i-1 not in vl:
            vl.add(i-1)
            Q.append([i-1, tim+1])

        if i*2 not in vl:
            vl.add(i*2)
            Q.append([i*2, tim+1])
print(tim)