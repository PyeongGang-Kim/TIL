from collections import deque
R, C = map(int, input().split())
nl = [list(input()) for _ in range(R)]
Q = deque()
for j in range(R):
    for i in range(C):
        if nl[j][i] == 'J':
            J = [i, j, False, 1]
        elif nl[j][i] == 'F':
            Q.append([i, j, True, 1])
Q.append(J)
D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
chk = False
while Q:
    x, y, o, cnt = Q.popleft()
    if not o and (not (1 <= x < C-1) or not (1 <= y < R-1)):
        chk = True
        break
    for dx, dy in D:
        tx, ty = x + dx, y + dy
        if 0 <= tx < C and 0 <= ty < R:
            # 갈 수 있고 불일때
            if o:
                if nl[ty][tx] == 'J' or nl[ty][tx] == '.':
                    nl[ty][tx] = 'F'
                    Q.append([tx, ty, True, cnt+1])
            else:
                if nl[ty][tx] == '.':
                    nl[ty][tx] = 'J'
                    Q.append([tx, ty, False, cnt+1])
if chk:
    print(cnt)
else:
    print('IMPOSSIBLE')