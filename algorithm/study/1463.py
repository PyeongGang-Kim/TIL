import sys
input = sys.stdin.readline
from collections import deque

nl = deque([int(input())])
vl = [False for _ in range(nl[0])]
cnt = 0
r = 0
if nl[0] == 1:
    print(0)
else:
    while not r:
        for i in range(len(nl)):
            if nl[0] == 1:
                r = cnt
                break
            tmp1, tmp2 = divmod(nl[0], 3)
            if not tmp2 and not vl[tmp1]:
                nl.append(tmp1)
                vl[tmp1] = True
            if not nl[0]&1 and not vl[nl[0]>>1]:
                nl.append(nl[0]>>1)
                vl[nl[0]>>1] = True
            if not vl[nl[0]-1]:
                nl.append(nl[0]-1)
                vl[nl[0]-1] = True

            nl.popleft()
        cnt += 1
    print(r)