import sys
from collections import deque
'''
처음부터 두 덩어리였을 경우
빙산이 다 녹아버린 경우 바로 끝내야함.

'''

def bfs(k):
    tmpcnt = 1
    tmpset = {(k[0], k[1])}
    Q = deque([[k[0], k[1]]])
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            tp = (x + dx, y + dy)
            if tp in ml:
                if tp not in tmpset:
                    Q.append(tp)
                    tmpset.add(tp)
                    tmpcnt += 1
    if tmpcnt == len(ml):
        return False
    else:
        return True


N, M = map(int, input().split())
ml = {}
for n in range(N):
    tmp = sys.stdin.readline().split()
    for m in range(M):
        if tmp[m] != '0':
            ml[(m, n)] = int(tmp[m])
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]

tmp = ml.popitem()
ml[tmp[0]] = tmp[1]
if bfs(tmp[0]):
    print(0)
else:

    r = 1
    chk = False
    while ml:
        tl = {}
        for p, v in ml.items():
            x, y = p
            cnt = 0
            for dx, dy in d:
                tx, ty = x + dx, y + dy
                if (tx, ty) not in ml:
                    cnt += 1
            tl[(x, y)] = cnt

        for p, v in tl.items():
            tmp = ml[p] - v
            if tmp > 0:
                ml[p] = tmp
            else:
                del ml[p]
        if ml:
            tmp = ml.popitem()
            ml[tmp[0]] = tmp[1]
            if bfs(tmp[0]):
                print(r)
                chk = True
                break
            r += 1
    if not chk:
        print(0)