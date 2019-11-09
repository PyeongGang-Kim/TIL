N = int(input())
nl = [list(input()) for _ in range(N)]
vl = [[0 for _ in range(N)] for _ in range(N)]

d = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
for j in range(N):
    for i in range(N):
        if nl[j][i] == '.':
            cnt = 0
            for dx, dy in d:
                tx, ty = i + dx, j + dy
                if 0 <= tx < N and 0 <= ty < N and nl[ty][tx] != '.':
                    cnt += int(nl[ty][tx])
            if cnt > 9:
                vl[j][i] = 'M'
            else:
                vl[j][i] = str(cnt)
        else:
            vl[j][i] = '*'
for i in range(N):
    print(''.join(vl[i]))