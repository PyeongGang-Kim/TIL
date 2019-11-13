from collections import deque
'''
사람 리스트
계단1[좌표, [사람인덱스, ]]
계단2[좌표, [사람인덱스, ]]
부분집합을 구해서 넣는다
넣고 나서 최종 시간 두개 찾고
큰 값을 결과에 반영
'''
dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    pl = []
    sl = []
    for j in range(N):
        for i in range(N):
            if nl[j][i] and nl[j][i] != 1:
                sl.append([i, j, nl[j][i]])

    vl = [[False for _ in range(N)] for _ in range(N)]
    vl[sl[0][1]][sl[0][0]] = True
    Q = deque([[sl[0][0], sl[0][1]]])
    while Q:
        x, y = Q.popleft()
        for dx, dy in dr:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx]:
                Q.append([tx, ty])
                vl[ty][tx] = True
                if nl[ty][tx] == 1:
                    pl.append([tx, ty])
    np = len(pl)
    r = 0xfffff
    for i in range(1<<np):
        sl1 = []
        sl2 = []
        for j in range(np):
            if 1<<j&i:
                sl1.append(abs(sl[0][0] - pl[j][0]) + abs(sl[0][1] - pl[j][1]))
            else:
                sl2.append(abs(sl[1][0] - pl[j][0]) + abs(sl[1][1] - pl[j][1]))
        sl2.sort()
        for i in range(3, len(sl1)):
            sl1[i] = max(sl1[i-3] + sl[0][2], sl1[i])
        for i in range(3, len(sl2)):
            sl2[i] = max(sl2[i-3] + sl[1][2], sl2[i])
        # print(sl1)
        # print(sl2)
        # print()
        if sl1:
            if sl2:
                r = min(max(sl1[-1]+sl[0][2], sl2[-1]+sl[1][2]), r)
            else:
                r = min(sl1[-1]+sl[0][2], r)
        else:
            if sl2:
                r = min(sl2[-1]+sl[1][2], r)
    print('#{} {}'.format(t, r+1))
