D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    tl = [list(map(int, input().split())) for _ in range(N)]
    cells = [[] for _ in range(12)]
    cells2 = [0 for _ in range(12)]
    cnt = 0
    # 세포가 태어난 시간, 활성화되는 시간, 죽는시간
    nl = [[[] for _ in range(1000)] for _ in range(1000)]
    for i in range(M):
        for j in range(N):
            if tl[j][i]:
                nl[j+500][i+500] = [0, tl[j][i], tl[j][i] << 1]
                cells[tl[j][i]].append([i+500, j+500])
                cnt += 1

    turn = 1

    while turn <= K:

        # for j in range(490, 510):
        #     tmp = [x if x else [0, 0, 0] for x in nl[j][490:510]]
        #     print(tmp)
        # cells[0]을 본다. 여기에 있는 세포들이 번식을 할 것.
        for x, y in cells[0]:
            life = nl[y][x][1] - nl[y][x][0]
            cells2[life-1] += 1
            for dx, dy in D:
                tx, ty = x + dx, y + dy
                if nl[ty][tx]:
                    if nl[ty][tx][0] == turn and nl[ty][tx][1] - nl[ty][tx][0] < life:
                        nl[ty][tx][1] = turn + life
                        nl[ty][tx][2] = turn + 2 * life
                else:
                    nl[ty][tx] = [turn, turn + life, turn + 2 * life]
                    cells[life+1].append([tx, ty])
                    cnt += 1
        cnt -= cells2[0]
        for i in range(11):
            cells[i], cells[i+1] = cells[i+1], cells[i]
            cells2[i], cells2[i+1] = cells2[i+1], cells2[i]
        cells.pop()
        cells2.pop()
        cells.append([])
        cells2.append(0)
        turn += 1
    print("#{} {}".format(tc, cnt))
