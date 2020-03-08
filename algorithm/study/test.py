from collections import deque

F, S, G, U, D = map(int, input().split())
if S == G:
    print(0)
else:

    Q = deque([[S, 1]])
    vl = [0 for i in range(F)]
    chk = False
    while Q:
        p, cnt = Q.popleft()
        t1 = p + U
        t2 = p - D
        if t1 == G or t2 == G:
            chk = True
            break

        if t1 < F:
            if not vl[t1]:
                Q.append([t1, cnt + 1])
                vl[t1] = True
        if t2 > 0:
            if not vl[t2]:
                Q.append([t2, cnt + 1])
                vl[t2] = True

    if chk:
        print(cnt)
    else:
        print('use the stairs')