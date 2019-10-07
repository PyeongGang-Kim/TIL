from collections import deque

F, S, G, U, D = map(int, input().split())

Q = deque([S, 0])
vl = [0 for 0 in range(F)]
while Q:
    p, cnt = Q.popleft()
    t1 = p+U
    t2 = p-D
    if t1 == G or t2 == G:
        pass


    if t1 < F:
        Q.append(t1)
    if t2 >= 0:
        Q.append(t2)
