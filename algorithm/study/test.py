def pos(idx, dep, offset):
    numNode = 1
    if nl[idx].lc != -1:
        numNode += pos(nl[idx].lc, dep + 1, offset)
    numNode += offset
    ml[dep][0] = min(ml[dep][0], numNode)
    ml[dep][1] = max(ml[dep][1], numNode)
    if nl[idx].rc != -1:
        numNode += pos(nl[idx].rc, dep + 1, numNode)
    return numNode-offset


class Node:
    root = -1


N = int(input())
nl = [Node() for _ in range(N+1)]
ml = [[10001, 0] for _ in range(N+1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    nl[a].lc = b
    nl[a].rc = c
    if b >= 0:
        nl[b].root = a
    if c >= 0:
        nl[c].root = a
for i in range(1, N+1):
    if nl[i].root == -1:
        pos(i, 1, 0)
        break

tmp = 1
maxdep = 0
maxwid = 0
while tmp <= N and ml[tmp][1]:
    tmp2 = ml[tmp][1]-ml[tmp][0]+1
    if tmp2 > maxwid:
        maxwid = tmp2
        maxdep = tmp
    tmp += 1

print(maxdep, maxwid)