from collections import deque
import sys
input = sys.stdin.readline

def printroute():
    if nl[n] != inf:
        ml2 = [[] for _ in range(n + 1)]
        for u in range(1, n+1):
            for v, w in ml[u]:
                ml2[v].append([u, w])
        pos = n
        r = []
        vl = [0] * (n+1)
        vl[n] = 1
        while 1:
            tmp = pos
            for u, w in ml2[pos]:
                if not vl[u] and w + nl[u] == nl[pos]:
                    r.append(str(pos))
                    pos = u
                    vl[u] = True
                    break
            if pos == 1:
                r.append('1')
                break
            if tmp == pos:
                print(-1)
                return
        print(' '.join(reversed(r)))
    else:
        print(-1)


def check():
    ml2 = [[] for _ in range(n + 1)]
    for u in range(1, n+1):
        for v, w in ml[u]:
            ml2[u].append([v, w])
    while Q:
        pos = Q.popleft()
        if pos == n:
            return True
        vl[pos] = 1
        for v, w in ml2[pos]:
            if not vl[v]:
                vl[v] = 1
                Q.append(v)
    return False

inf = 0xfffffff
n, m = map(int, input().split())
nl = [inf for _ in range(n+1)]
ml = [[] for _ in range(n + 1)]
while m:
    m -= 1
    u, v, w = map(int, input().split())
    ml[u].append([v, w])

i = n - 1
nl[1] = 0
while i:
    i -= 1
    update = False
    for u in range(1, n):
        for v, w in ml[u]:
            if nl[u] != inf:
                if nl[v] != inf:
                    if nl[u] + w > nl[v]:
                        nl[v] = nl[u] + w
                        update = True
                else:
                    nl[v] = nl[u] + w
    if not update:
        break

Q = deque()

vl = [0] * (n + 1)
if update:
    for i in range(1, n):
        for v, w in ml[u]:
            if nl[u] != inf:
                if nl[u] + w > nl[v]:
                    Q.append(u)
                    vl[u] = 1

    if check():
        print(-1)
    else:
        printroute()
else:
    printroute()

