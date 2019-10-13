import sys
'''
터질 수 있는 뿌요들의 좌표를 확인하기 위해 각 좌표들에 대해 bfs를 실시한다.
터질 수 있는 뿌요들의 좌표를 따로 저장해 둔다.
모두 확인했으면 저장된 좌표(제거할 뿌요들의 좌표)를 확인한다.
만약 제거할 뿌요가 없으면 종료
제거할 뿌요가 있으면 모두 제거한 후 연쇄를 +1 해준다.
뿌요들을 바닥에 붙인다.
처음으로 되돌아간다.
'''
d = ((0, 1), (0, -1), (-1, 0), (1, 0))
N, M = 12, 6
ram = range(M)
ran = range(N)
vl = [[False for _ in ram] for _ in ran]
nl = []
for j in ran:
    nl.append(['' if s == '.' else s for s in sys.stdin.readline().strip()])
high = [0] * 6
r = 0
while 1:
    pl = []
    for i in ram:
        for j in range(N-1, high[i]-1, -1):
            if not vl[j][i]:
                vl[j][i] = True
                if nl[j][i]:
                    idx = 0
                    rear = 1
                    Q = [(i, j)]
                    cc = nl[j][i]
                    while idx < rear:
                        x, y = Q[idx]
                        idx += 1
                        for dx, dy in d:
                            tx, ty = x + dx, y + dy
                            if 0 <= tx < M and high[tx] <= ty < N and not vl[ty][tx] and nl[ty][tx] == cc:
                                vl[ty][tx] = True
                                Q.append((tx, ty))
                                rear += 1
                    if idx > 3:
                        pl = pl + Q

    if pl:
        #연쇄 +1
        r += 1
        #뿌요 제거
        for x, y in pl:
            nl[y][x] = ''
        #뿌요 바닥에 붙이기
        tmphigh = [N-1] * M
        for i in ram:
            for j in range(N-1, high[i]-1, -1):
                if not nl[j][i]:
                    k = j - 1
                    while k >= high[i]:
                        if nl[k][i]:
                            nl[k][i], nl[j][i] = nl[j][i], nl[k][i]
                            tmphigh[i] = j
                            break
                        k -= 1
                else:
                    tmphigh[i] = j
        for i in ram:
            high[i] = tmphigh[i]
        for i in ram:
            for j in range(N-1, high[i]-1, -1):
                vl[j][i] = False
    else:
        break
print(r)