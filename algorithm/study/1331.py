D = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
     '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}


dr = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]

vl = [[False for _ in range(6)] for _ in range(6)]
nl = [input() for _ in range(36)]
nl.append(nl[0])
cx, cy = D[nl[0][0]], D[nl[0][1]]
cnt = 0
for i in range(1, 37):
    for dx, dy in dr:
        tx, ty = cx + dx, cy + dy
        if tx == D[nl[i][0]] and ty == D[nl[i][1]] and not vl[ty][tx]:
            cx, cy = tx, ty
            cnt += 1
            vl[ty][tx] = True
            break
    if cnt != i:
        break

if cnt != 36:
    print('Invalid')
else:
    print('Valid')

